# CLI TICKETING SYSTEM
A lightweight command line ticketing system that simulates real helpdesk workflows including ticket creation, updates, and lifecycle tracking using JSON

## PURPOSE
This program was built to simulate real-world IT support workflows and demonstrate practical system design skills using Python, file-based persistence, and a command-line interface.

## FEATURES

- Create support tickets via CLI
- View all tickets in a readable format
- Update ticket status (Open, In Progress, Closed)
- Close tickets (soft delete via status change)
- Persisent storage using JSON
- Simple command-line interface for interaction

## HOW TO USE:

Run commands from the terminal:

```bash
ticket create
ticket list
ticket update <ticket id>
ticket close <ticket id>

---

## EXAMPLE OUTPUT
```md id="c8v4xp"
## Example Output
```bash
ID: 1
Title: WiFi issue
Description: User cannot connect to internet
Status: Open
Priority: High

## TECH STACK
- Python 3
- JSON
- Ubuntu (WSL)
