from api.client import get_depots, get_vehicles, get_token
from scheduler.scheduler import schedule_tasks
from logger.logger import log

def main():
    token = get_token()

    try:
        log("backend", "info", "handler", "Application started", token)

        depots = get_depots()
        log("backend", "info", "handler", "Fetched depots", token)

        vehicles = get_vehicles()
        log("backend", "info", "handler", "Fetched vehicles", token)

        result = schedule_tasks(depots, vehicles, token)

        log("backend", "info", "handler", "Scheduling completed", token)

        print("\n=== FINAL SCHEDULE ===")

        for depot_id, data in result.items():
            # skip special keys
            if depot_id in ["unassigned", "overall_priority"]:
                continue

            print(f"\nDepot {depot_id}")
            print(f"Total Priority: {data['total_priority']}")

            for task in data["tasks"]:
                print(f"Vehicle {task['id']} | Duration: {task['duration']} | Priority: {task['priority']}")

        # unassigned vehicles
        print("\nUnassigned Vehicles:")
        for v in result.get("unassigned", []):
            print(f"Vehicle {v['id']} | Duration: {v['duration']} | Priority: {v['priority']}")

        # overall summary
        print(f"\nOverall Priority Achieved: {result.get('overall_priority', 0)}")

    except Exception as e:
        log("backend", "error", "handler", str(e), token)

if __name__ == "__main__":
    main()