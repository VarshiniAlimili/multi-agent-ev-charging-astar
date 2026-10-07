
class EV:

    def __init__(self, name, battery, target,
                 charging_time, power, priority):

        self.name = name
        self.battery = battery
        self.target = target
        self.charging_time = charging_time
        self.power = power
        self.priority = priority


class State:

    def __init__(self, assignment, time_remaining=None):

        self.assignment = tuple(assignment)

        if time_remaining is None:

            self.time_remaining = tuple(0 for _ in assignment)

        else:

            self.time_remaining = tuple(time_remaining)


class ChargingStation:

    def __init__(self, slots, power_limit):

        self.slots = slots
        self.power_limit = power_limit

    # -----------------------------------------
    # Generate possible next states
    # -----------------------------------------

    def get_neighbors(self, evs, state):

        neighbors = []

        current = state.assignment

        # Find occupied slots
        used_slots = set()

        for slot in current:

            if slot > 0:
                used_slots.add(slot)

        # Find free slots
        free_slots = []

        for slot in range(1, self.slots + 1):

            if slot not in used_slots:
                free_slots.append(slot)

        # Assign only WAITING EVs
        for i, ev in enumerate(evs):

            # 0 = waiting
            # positive number = charging
            # -1 = completed

            if current[i] != 0:
                continue

            for slot in free_slots:

                new_assignment = list(current)

                new_assignment[i] = slot

                # Copy existing charging times
                new_time = list(state.time_remaining)

                # Start charging this EV
                new_time[i] = ev.charging_time

                new_state = State(
                    new_assignment,
                    new_time
                )

                # Check power constraint
                if self.valid_state(evs, new_state):

                    neighbors.append(new_state)

        return neighbors
    def advance_time(self, state):

        new_assignment = list(state.assignment)

        new_time = list(state.time_remaining)

        for i in range(len(new_time)):

            if new_time[i] > 0:

                new_time[i] -= 1

                # Charging completed
                if new_time[i] == 0:

                    new_assignment[i] = -1

        return State(new_assignment, new_time)
    # -----------------------------------------
    # Check whether a state is valid
    # -----------------------------------------

    def valid_state(self, evs, state):

        total_power = 0

        for i, slot in enumerate(state.assignment):

            if slot > 0:
                total_power += evs[i].power

        if total_power <= self.power_limit:
            return True

        return False

    # -----------------------------------------
    # Calculate g(n)
    # -----------------------------------------

    def calculate_cost(self, evs, state):

        cost = 0

        for i, slot in enumerate(state.assignment):

            # Only currently charging EVs
            if slot > 0:

                urgency = (
                    (100 - evs[i].battery)
                    + (20 * evs[i].priority)
                )

                cost += urgency

        return cost
    # -----------------------------------------
    # Calculate h(n)
    # -----------------------------------------

    def calculate_heuristic(self, evs, state):

        heuristic = 0

        for i, slot in enumerate(state.assignment):

            # Only waiting EVs
            if slot == 0:

                urgency = (
                    (100 - evs[i].battery)
                    + (20 * evs[i].priority)
                )

                heuristic += urgency

        return heuristic
    # -----------------------------------------
    # Calculate f(n)
    # -----------------------------------------

    def calculate_f(self, evs, state):

        g = self.calculate_cost(evs, state)

        h = self.calculate_heuristic(evs, state)

        f = g + h

        return f

    # -----------------------------------------
    # Find state with lowest f(n)
    # -----------------------------------------

    def get_best_state(self, evs, states):

        best_state = None
        best_f = float("inf")
        best_urgency = -1

        for state in states:

            f_value = self.calculate_f(evs, state)

        # Calculate urgency of EVs that are assigned
            assigned_urgency = 0

            for i, slot in enumerate(state.assignment):

                if slot > 0:

                    urgency = (
                        (100 - evs[i].battery)
                        + (20 * evs[i].priority)
                    )

                    assigned_urgency += urgency

        # Select lower f(n)
        # If f(n) is equal, select higher urgency
            if (f_value < best_f or
                    (f_value == best_f and
                    assigned_urgency > best_urgency)):

                best_f = f_value
                best_state = state
                best_urgency = assigned_urgency

        return best_state, best_f

    # -----------------------------------------
    # A* Search
    # -----------------------------------------
    def a_star_search(self, evs, initial_state):

        current_state = initial_state

        path = [current_state.assignment]

        while True:

            # Check whether all EVs are completed
            if all(slot == -1 for slot in current_state.assignment):

                print("\nAll EVs completed charging.")
                break

            # Try to assign waiting EVs
            neighbors = self.get_neighbors(evs, current_state)

            if neighbors:

                current_state, f_value = self.get_best_state(
                    evs, neighbors
                )

                path.append(current_state.assignment)

                print("\nSelected State:", current_state.assignment)
                print("Time Remaining:", current_state.time_remaining)
                print("F(n):", f_value)

            else:

                # No free slot.
                # Advance charging by one time unit.

                if any(t > 0 for t in current_state.time_remaining):

                    current_state = self.advance_time(current_state)

                    path.append(current_state.assignment)

                    print("\nTime advanced by 1 unit")
                    print("Current State:", current_state.assignment)
                    print("Time Remaining:", current_state.time_remaining)

                else:

                    print("\nNo valid actions remaining.")
                    break

        print("\nA* Search Path")
        print("-" * 40)

        for step, state in enumerate(path):

            print("Step", step, ":", state)

        return current_state


# ==================================================
# CREATE EV AGENTS
# ==================================================

ev1 = EV("EV1", 20, 80, 4, 30, 4)

ev2 = EV("EV2", 65, 90, 3, 20, 1)

ev3 = EV("EV3", 30, 80, 5, 20, 3)

evs = [ev1, ev2, ev3]


# ==================================================
# CREATE CHARGING STATION
# ==================================================

station = ChargingStation(2, 70)

initial_state = State(
    [0, 0, 0],
    [0, 0, 0]
)


# ==================================================
# DISPLAY EV INFORMATION
# ==================================================

print("=" * 60)

print("          MULTI-AGENT EV CHARGING SYSTEM")

print("=" * 60)

print("\nEV AGENT INFORMATION")

print("-" * 60)

for ev in evs:

    print(
        ev.name,
        "| Battery:", ev.battery, "%",
        "| Target:", ev.target, "%",
        "| Charging Time:", ev.charging_time,
        "| Power:", ev.power, "kW",
        "| Priority:", ev.priority
    )


# ==================================================
# DISPLAY STATION INFORMATION
# ==================================================

print("\nCHARGING STATION")

print("-" * 60)

print("Number of Slots :", station.slots)

print("Power Limit     :", station.power_limit, "kW")


# ==================================================
# INITIAL STATE
# ==================================================

print("\nINITIAL STATE")

print("-" * 60)

print("State:", initial_state.assignment)

print("\nState Representation:")

print("0 = Waiting")

print("1 = Slot 1")

print("2 = Slot 2")


# ==================================================
# TEST CURRENT STATE
# ==================================================
state1 = State(
    [1, 0, 0],
    [4, 0, 0]
)

print("\nCURRENT STATE")

print("-" * 60)

print("Assignment:", state1.assignment)

print("Time Remaining:", state1.time_remaining)

print("\nInterpretation:")

print("EV1 -> Slot 1 | Time Remaining:", state1.time_remaining[0])

print("EV2 -> Waiting | Time Remaining:", state1.time_remaining[1])

print("EV3 -> Waiting | Time Remaining:", state1.time_remaining[2])


# ==================================================
# GENERATE NEXT STATES
# ==================================================

neighbors = station.get_neighbors(evs, state1)

print("\nPOSSIBLE NEXT STATES")

print("-" * 60)

for state in neighbors:

    print("Assignment     :", state.assignment)

    print("Time Remaining :", state.time_remaining)

    print()
print("\nTIME PROGRESSION TEST")
print("-" * 60)

test_state = State(
    [1, 0, 2],
    [4, 0, 5]
)

print("Before 1 time unit:")
print("Assignment     :", test_state.assignment)
print("Time Remaining :", test_state.time_remaining)

next_state = station.advance_time(test_state)

print("\nAfter 1 time unit:")
print("Assignment     :", next_state.assignment)
print("Time Remaining :", next_state.time_remaining)
# ==================================================
# A* CALCULATION
# ==================================================

cost = station.calculate_cost(evs, state1)

heuristic = station.calculate_heuristic(evs, state1)

f_value = station.calculate_f(evs, state1)

print("\nA* CALCULATION FOR CURRENT STATE")

print("-" * 60)

print("g(n) - Current Cost :", cost)

print("h(n) - Heuristic    :", heuristic)

print("f(n) = g(n) + h(n) :", f_value)


# ==================================================
# BEST NEXT STATE
# ==================================================

best_state, best_f = station.get_best_state(
    evs, neighbors
)

print("\nBEST NEXT STATE")

print("-" * 60)

print("State :", best_state.assignment)

print("f(n)  :", best_f)


# ==================================================
# RUN A* SEARCH
# ==================================================

print("\n")

print("=" * 60)

print("                    A* SEARCH")

print("=" * 60)

final_state = station.a_star_search(
    evs,
    initial_state
)


# ==================================================
# FINAL ALLOCATION
# ==================================================

print("\nFINAL RESULT")
print("=" * 60)

print("Final State:", final_state.assignment)

print("\nEV Status:")

for i, slot in enumerate(final_state.assignment):

    if slot == -1:

        print(evs[i].name, "-> COMPLETED")

    elif slot == 0:

        print(evs[i].name, "-> WAITING")

    else:

        print(evs[i].name, "-> CHARGING IN SLOT", slot)

print("\nRemaining Charging Time:")
print(final_state.time_remaining)

# ==================================================
# EDGE CASE 1
# More EVs than charging slots
# ==================================================

print("\n")
print("=" * 60)
print("EDGE CASE 1: MORE EVs THAN AVAILABLE SLOTS")
print("=" * 60)

edge_station = ChargingStation(1, 70)

edge_initial_state = State(
    [0, 0, 0],
    [0, 0, 0]
)

print("\nNumber of EVs   :", len(evs))
print("Available Slots :", edge_station.slots)

if len(evs) > edge_station.slots:

    print("\nResult:")
    print("There are more EVs than available charging slots.")
    print("Some EVs must wait until a slot becomes available.")

else:

    print("\nResult:")
    print("All EVs can be assigned immediately.")

# ==================================================
# EDGE CASE 2
# Insufficient Charging Power
# ==================================================

print("\n")
print("=" * 60)
print("EDGE CASE 2: INSUFFICIENT CHARGING POWER")
print("=" * 60)

power_station = ChargingStation(2, 20)

power_initial_state = State(
    [0, 0, 0],
    [0, 0, 0]
)

print("\nStation Power Limit:", power_station.power_limit, "kW")

print("EV1 Requested Power:", ev1.power, "kW")

print("\nChecking EV1...")

if ev1.power > power_station.power_limit:

    print("Result: EV1 cannot be assigned.")
    print("Reason: Required power is greater than station limit.")

else:

    print("Result: EV1 can be assigned.")
# ==================================================
# END
# ==================================================

print("\n")

print("=" * 60)

print("              SIMULATION COMPLETE")

print("=" * 60)
# ==================================================
# WORKING CASE 2
# SINGLE SLOT COMPETITION
# ==================================================

print("\n")
print("=" * 60)
print("WORKING CASE 2: SINGLE SLOT COMPETITION")
print("=" * 60)

single_slot_station = ChargingStation(1, 70)

single_slot_initial = State(
    [0, 0, 0],
    [0, 0, 0]
)

print("\nNumber of EVs:", len(evs))
print("Available Slots:", single_slot_station.slots)
print("Power Limit:", single_slot_station.power_limit, "kW")

print("\nResult:")
print("Only one EV can charge at a time.")
print("Other EVs must wait until the slot becomes available.")

single_slot_station.a_star_search(
    evs,
    single_slot_initial
)