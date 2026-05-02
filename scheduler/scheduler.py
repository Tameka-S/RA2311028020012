from logger.logger import log

def schedule_tasks(depots, vehicles, token):
    log("backend", "info", "scheduler", "Scheduling started", token)

    # sort depots 
    depots.sort(key=lambda x: x["mechanicHours"], reverse=True)

    # validate vehicles 
    vehicles = [v for v in vehicles if v.get("duration", 0) > 0 and v.get("priority", 0) > 0]

    # safe sorting 
    vehicles.sort(
        key=lambda x: (x["priority"] / x["duration"]) if x["duration"] > 0 else 0,
        reverse=True
    )

    result = {}
    used = set()

    for depot in depots:
        log(
            "backend",
            "info",
            "scheduler",
            f"Processing depot {depot['id']} with {depot['mechanicHours']} hours",
            token
        )
        remaining = depot["mechanicHours"]
        assigned = []
        total_priority = 0

        for vehicle in vehicles:
            if vehicle["id"] not in used and vehicle["duration"] <= remaining:
                assigned.append(vehicle)
                used.add(vehicle["id"])
                remaining -= vehicle["duration"]
                total_priority += vehicle["priority"]

                log(
                    "backend",
                    "debug",
                    "scheduler",
                    f"Assigned vehicle {vehicle['id']} to depot {depot['id']}",
                    token
                )

        result[depot["id"]] = {
            "tasks": assigned,
            "total_priority": total_priority
        }

    # track unassigned vehicles
    unassigned = [v for v in vehicles if v["id"] not in used]
    result["unassigned"] = unassigned

    # overall system metric
    overall_priority = sum(
        d["total_priority"] for d in result.values() if isinstance(d, dict)
    )
    result["overall_priority"] = overall_priority

    log("backend", "info", "scheduler", "Scheduling completed", token)

    return result