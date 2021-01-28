# Shared expenses tracking and management.
*Implementation of a basic shared expanses tracker and management system in python.*
## Use

- Create participants
- Create event
- Add transactions
- Reconcile

## Example: 

```py
annie = Member('Annie')
sally = Member('Sally')
bill = Member('Bill')

concert = Event('Concert', [annie, bill, sally])
concert.add_transaction('tickets', 180, annie)
concert.add_transaction('dinner', 75, sally)
concert.add_transaction('drinks', 19, bill)
concert.add_transaction('taxi', 16, bill)

concert.reconcile()
```
## Requirements

1.  An individual can only participate in a single event at any given time.
    
2.  Assume that all members share all transactions equally.
    
3.  Set-up:
    

	-  Declare named individuals to participate in the event/activity.
    
	-  Setup the activity: indicating the participating individuals.
    

4.  Code to add transactions. A transaction has (see Appendix):
    

	-  name: string
    
	-  amount: a positive number
    
	-  payee: member ID
    

5.  Code to print the reconciliation, i.e. total cost, cost each, who owes who what?
