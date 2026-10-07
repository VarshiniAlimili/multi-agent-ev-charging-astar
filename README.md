# Multi-Agent EV Charging Station Management Using A* Search

## Project Overview

This project presents a **Multi-Agent EV Charging Station Management System** that uses an **A*-guided search approach** to manage multiple electric vehicles competing for limited charging resources.

Each electric vehicle (EV) is modeled as an independent agent with its own battery level, target battery level, charging time, power requirement, and priority. The charging station has a limited number of charging slots and a maximum power capacity.

The system evaluates feasible charging assignments and selects suitable states based on EV urgency while satisfying charging-slot and power constraints.

## Problem Statement

When multiple EVs request charging at the same time, a charging station must decide which EVs should receive the available charging slots. Since the number of slots and available electrical power are limited, assigning all EVs simultaneously may not be possible.

The objective is to allocate charging resources efficiently while ensuring that the station's constraints are not violated.

## Objectives

- Model EVs as independent agents.
- Represent the charging system using states.
- Allocate limited charging slots among competing EVs.
- Respect the charging station's power limit.
- Use A*-guided search to evaluate feasible states.
- Consider EV urgency and priority during allocation.
- Handle completed EVs and release their charging slots.
- Demonstrate normal and edge-case scenarios.

## EV Configuration

| EV | Battery | Target | Charging Time | Power | Priority |
|---|---:|---:|---:|---:|---:|
| EV1 | 20% | 80% | 4 | 30 kW | 4 |
| EV2 | 65% | 90% | 3 | 20 kW | 1 |
| EV3 | 30% | 80% | 5 | 20 kW | 3 |

The main charging station has **2 charging slots** and a **70 kW power limit**.

## State Representation

Each EV is represented using a state value:

- `0` → EV is waiting
- `1` → EV is charging in Slot 1
- `2` → EV is charging in Slot 2
- `-1` → EV has completed charging

The initial state is:

```text
(0, 0, 0)
```

The goal state is:

```text
(-1, -1, -1)
```

which indicates that all EVs have completed charging.

## A*-Guided Search

The system evaluates feasible states using:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` represents the urgency of EVs currently charging.
- `h(n)` represents the urgency of waiting EVs.
- `f(n)` is the combined evaluation value.

EV urgency is calculated using:

```text
Urgency = (100 - Battery) + (20 × Priority)
```

The search considers only states that satisfy the charging-slot and power constraints.

## Resource Constraints

The system checks:

1. The number of simultaneously charging EVs cannot exceed the number of available slots.
2. The total power requirement of active EVs cannot exceed the station power limit.
3. Completed EVs cannot be assigned again.
4. When an EV completes charging, its charging slot becomes available for another waiting EV.

## Working Cases

### Working Case 1

- 3 EVs
- 2 charging slots
- 70 kW power limit

The system successfully allocates charging slots and all three EVs eventually complete charging.

Final state:

```text
(-1, -1, -1)
```

### Working Case 2

- 3 EVs
- 1 charging slot
- 70 kW power limit

Since only one EV can charge at a time, the EVs are processed sequentially. All three EVs eventually complete charging.

## Edge Cases

### Edge Case 1 — More EVs Than Slots

When the number of EVs is greater than the number of available charging slots, some EVs remain in the waiting state until a slot becomes available.

### Edge Case 2 — Insufficient Charging Power

When the station power limit is 20 kW and an EV requires 30 kW, the assignment is rejected because:

```text
30 kW > 20 kW
```

This prevents an invalid charging assignment.

## Technologies Used

- Python
- Artificial Intelligence
- A* Search
- Multi-Agent Systems
- State-Space Search

## Project Structure

```text
multi-agent-ev-charging-astar/
│
├── README.md
├── main.py
├── system_architecture.png
├── astar_state_space.png
├── ev_charging_allocation.png
└── requirements.txt
```

## Results

The system successfully demonstrates:

- Multi-agent interaction through shared charging resources.
- A*-guided state evaluation.
- Charging-slot management.
- Power constraint handling.
- Sequential charging when resources are limited.
- Handling of invalid charging assignments.
- Completion of all EV charging requests in successful cases.

## Conclusion

The project demonstrates how artificial intelligence search techniques can be applied to a practical multi-agent resource allocation problem. By combining EV priorities, charging requirements, limited charging slots, power constraints, and charging-time progression, the system provides a simple simulation of intelligent EV charging station management.
