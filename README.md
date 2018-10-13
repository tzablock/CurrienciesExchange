Hourly aggregated bid/ask exchange rates for each currency pair (open, high, low, close rates).
bid - sell, it's rate for which you can sell currency
ask - buy, it's rate for which you can buy currency
open - opening price
close - closing price
high - the highest price
low - the lowest price
tick - a tick is when the last transaction is at a price different to the one before it. this could be a buyer in the books being matched or a seller in the books being matched. the order book can change a million times and the highest bid and lowest sell change and change and change... but this is not a tick. only when a transaction occurs and the price is different to the previous does a 'tick' occur.
Data description:
symbol	    string	Symbols of the base/quote currencies, e.g. USD/CAD. See the Currency Pairs section below for a complete list of symbols.
date	    date	Date of the start of the reporting period. Time zone is UTC.
hour	    int	    Hour (0-23) at the start of the reporting period (UTC). For example, hour = 17 indicates reporting period from 17:00 to 18:00 (UTC)	
openbid	    double	Bid rate at the start of the reporting period		
highbid	    double	Highest bid rate during the reporting period		
lowbid	    double	Lowest bid rate during the reporting period		
closebid    double	Bid rate at the closing of the reporting period		
openask	    double	Ask rate at the start of the reporting period		
highask	    double	Highest ask rate during the reporting period		
lowask	    double	Lowest ask rate during the reporting period		
closeask    double	Ask rate at the closing of the reporting period		
totalticks  int	    Total change in ticks between the exchange rates of a transaction and the last one during the hour, i.e., an index of volatility, for the reporting hour

SYMBOL	CURRENCY PAIR
AUD/CAD	Australian Dollar/Canadian Dollar
AUD/CHF	Australian Dollar/Swiss Franc
AUD/JPY	Australian Dollar/Japanese Yen
AUD/NZD	Australian Dollar/New Zealand Dollar
AUD/USD	Australian Dollar/US Dollar
CAD/CHF	Canadian Dollar/Swiss Franc
CAD/JPY	Canadian Dollar/Japanese Yen
CHF/JPY	Swiss Franc/Japanese Yen
EUR/AUD	Euro/Australian Dollar
EUR/CAD	Euro/Canadian Dollar
EUR/CHF	Euro/Swiss Franc
EUR/GBP	Euro/British Pound
EUR/JPY	Euro/Japanese Yen
EUR/NOK	Euro/Norwegian Krone
EUR/NZD	Euro/New Zealand Dollar
EUR/SEK	Euro/Swedish Krona
EUR/TRY	Euro/Turkey Lira
EUR/USD	Euro/US Dollar
GBP/AUD	British Pound/Australian Dollar
GBP/CAD	British Pound/Canadian Dollar
GBP/CHF	British Pound/Swiss Franc
GBP/JPY	British Pound/Japanese Yen
GBP/NZD	British Pound/New Zealand Dollar
GBP/USD	British Pound/US Dollar
NZD/CAD	New Zealand Dollar/Canadian Dollar
NZD/CHF	New Zealand Dollar/Swiss Franc
NZD/JPY	New Zealand Dollar/Japanese Yen
NZD/USD	New Zealand Dollar/US Dollar
TRY/JPY	Turkey Lira/Japanese Yen
USD/CAD	US Dollar/Canadian Dollar
USD/CHF	US Dollar/Swiss Franc
USD/CNH	US Dollar/Chinese Yuan
USD/JPY	US Dollar/Japanese Yen
USD/MXN	US Dollar/Mexican Peso
USD/NOK	US Dollar/Norwegian Krone
USD/SEK	US Dollar/Swedish Krona
USD/TRY	US Dollar/Turkey Lira
USD/ZAR	US Dollar/South African Rand
ZAR/JPY	South African Rand/Japanese Yen

Tasks:
1. the highest, lowest opening price for every currency
2. the highest, lowest closing price for every currency
3. the biggest diffrence in opening and closing price for every currency
4. replace symbol by names(do own collection andbrodcast it)

4. diagram for 3. (all diffs by days for every day), by added by user currencys exchange
5. diagram for choosen by user currencys, and change by time(bid, ask separate)
6. the biggest diffrency by carrencys segregated in diagram(ever appered)
7. Open-high-low-close chart (https://en.wikipedia.org/wiki/Open-high-low-close_chart)
8. bid/ask value for choosen by user currency to all others 