#!/usr/bin/env python3

import sys
import json
from datetime import datetime

# Variables
def load_tickets():
	with open("tickets.json", "r") as file:
		return json.load(file)
def save_tickets(tickets):
	with open("tickets.json", "w") as file:
		json.dump(tickets, file, indent=4)

# create tickets
def create_ticket():
	title = input("Title: ")
	description = input("Description: ")
	priority = input("Priority (Low/Medium/High): ")

	tickets = load_tickets()
	
	# Generate ID
	ticket_id = len(tickets) + 1

	new_ticket = {
		"id": ticket_id,
		"title": title,
		"description": description,
		"priority": priority,
		"status": "Open",
		"created_at": str(datetime.now()),
		"history": ["Ticket created"]
	}

	tickets.append(new_ticket)
	save_tickets(tickets)
	
	print(f"Ticket #{ticket_id} created successfully")

# list tickets
def list_tickets():
	tickets = load_tickets()
	
	if len(tickets) == 0:
		print("No tickets found.")
		return

	print("\n--- TICKETS ---\n")

	for ticket in tickets:
		print(f"ID: {ticket['id']}")
		print(f"Title: {ticket['title']}")
		print(f"Priority: {ticket['priority']}")
		print(f"Status: {ticket['status']}")
		print("-" * 20)

# update tickets
def update_ticket(ticket_id):
	tickets = load_tickets()

	#Find ticket
	for ticket in tickets:
		if ticket["id"] == ticket_id:
			
			print(f"Current status: {ticket['status']}")
			print("O = Open, P = In Progress, R = Resolved")
			
			new_status = input("Enter new status (O / P / R): ")
		
			ticket["status"] = new_status
			ticket["history"].append(f"Status changed to {new_status}")

			save_tickets(tickets)

			print(f"Ticket #{ticket_id} updated successfully")
			return

	print("Ticket not found")

# close tickets
def close_ticket(ticket_id):
	tickets = load_tickets()

	for ticket in tickets:
		if ticket["id"] == ticket_id:

			if ticket["status"] == "Closed":
				print(f"Ticket #{ticket_id} is already closed.")
				return

			ticket["status"] = "Closed"
			ticket["history"].append("Ticket closed")

			save_tickets(tickets)

			print(f"Ticket #{ticket_id} closed successfully")
			return

	print("Ticket not found")

# Check if user provided a command
if len(sys.argv) < 2:
	print("Usage:")
	print("  create   - Create a ticket")
	print("  list   - List tickets")
	print("  update   - Update a ticket")
	sys.exit()

# Get the command
command = sys.argv[1]

# Handle commands
if command == "create":
	create_ticket()
elif command == "list":
	list_tickets()
elif command == "update":
	if len(sys.argv) < 3:
		print("Usage: update <ticket_id>")
	else:
		update_ticket(int(sys.argv[2]))
elif command == "close":
	if len(sys.argv) < 3:
		print("Usage: close <ticket_id>")
	else:
		close_ticket(int(sys.argv[2]))
else:
	print("Unknown command")
