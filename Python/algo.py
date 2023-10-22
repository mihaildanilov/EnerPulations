from collections import deque
from typing import List, Dict, Any

battery_capacity = 200  # 200 kWh
charging_speed = 0.2 # 20% / H
starting_battery = 0.2 # filled percentage
charging_speed_kwh = battery_capacity * charging_speed  # 40 kWh
starting_battery_kwh = battery_capacity * starting_battery  # 80 kWh
min_profit_threshold = 0.02
min_battery = 0.15
max_battery = 0.95

data = [
  {
    "hour": "00:00",
    "price": "0.040150",
    "day": "22-10-2023"
  },
  {
    "hour": "01:00",
    "price": "0.095690",
    "day": "22-10-2023"
  },
  {
    "hour": "02:00",
    "price": "0.030360",
    "day": "22-10-2023"
  },
  {
    "hour": "03:00",
    "price": "0.018610",
    "day": "22-10-2023"
  },
  {
    "hour": "04:00",
    "price": "0.015630",
    "day": "22-10-2023"
  },
  {
    "hour": "05:00",
    "price": "0.018350",
    "day": "22-10-2023"
  },
  {
    "hour": "06:00",
    "price": "0.034320",
    "day": "22-10-2023"
  },
  {
    "hour": "07:00",
    "price": "0.040010",
    "day": "22-10-2023"
  },
  {
    "hour": "08:00",
    "price": "0.058200",
    "day": "22-10-2023"
  },
  {
    "hour": "09:00",
    "price": "0.099310",
    "day": "22-10-2023"
  },
  {
    "hour": "10:00",
    "price": "0.114590",
    "day": "22-10-2023"
  },
  {
    "hour": "11:00",
    "price": "0.148930",
    "day": "22-10-2023"
  },
  {
    "hour": "12:00",
    "price": "0.076700",
    "day": "22-10-2023"
  },
  {
    "hour": "13:00",
    "price": "0.099550",
    "day": "22-10-2023"
  },
  {
    "hour": "14:00",
    "price": "0.148930",
    "day": "22-10-2023"
  },
  {
    "hour": "15:00",
    "price": "0.075420",
    "day": "22-10-2023"
  },
  {
    "hour": "16:00",
    "price": "0.081370",
    "day": "22-10-2023"
  },
  {
    "hour": "17:00",
    "price": "0.095740",
    "day": "22-10-2023"
  },
  {
    "hour": "18:00",
    "price": "0.124410",
    "day": "22-10-2023"
  },
  {
    "hour": "19:00",
    "price": "0.135510",
    "day": "22-10-2023"
  },
  {
    "hour": "20:00",
    "price": "0.138940",
    "day": "22-10-2023"
  },
  {
    "hour": "21:00",
    "price": "0.124690",
    "day": "22-10-2023"
  },
  {
    "hour": "22:00",
    "price": "0.112470",
    "day": "22-10-2023"
  },
  {
    "hour": "23:00",
    "price": "0.102180",
    "day": "22-10-2023"
  },
  {
    "hour": "00:00",
    "price": "0.095690",
    "day": "23-10-2023"
  }
]



def optimize_action_plan(data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    # Sort data by price for first pass
    sorted_data = sorted(data, key=lambda x: float(x['price']))
    
    # Initialize variables for first pass
    potential_buy_hours = set()
    potential_sell_hours = set()
    
    # First Pass: Identify potential buy and sell intervals
    for entry in sorted_data:
        hour = entry['hour']
        day = entry['day']
        price = float(entry['price'])
        
        # Potential buy if price is low
        if price <= float(sorted_data[len(sorted_data) // 4]['price']):
            potential_buy_hours.add((hour, day))
            
        # Potential sell if price is high
        if price >= float(sorted_data[3 * len(sorted_data) // 4]['price']):
            potential_sell_hours.add((hour, day))
    
    # Initialize variables for second pass
    battery_kwh = starting_battery_kwh
    action_plan = []
    total_profit = 0.0
    highest_buy_price = 0.0
    last_buy_hour = None
    
    # Second Pass: Generate action plan
    for entry in data:
        hour = entry['hour']
        day = entry['day']
        price = float(entry['price'])
        action = 'HOLD'
        selling_price = None
        battery_percentage = (battery_kwh / battery_capacity) * 100  # Added

        # Check against potential buy/sell intervals
        if (hour, day) in potential_buy_hours and (last_buy_hour is None or hour != last_buy_hour):
            # Smarter buying: Only buy if there's a reasonable expectation to sell later
            if any(h > hour for h, d in potential_sell_hours if d == day):
                charge_amount_kwh = min(charging_speed_kwh, battery_capacity * max_battery - battery_kwh)
                battery_kwh += charge_amount_kwh
                battery_percentage += charge_amount_kwh / battery_capacity * 100  # Added
                action = 'BUY'
                highest_buy_price = max(highest_buy_price, price)
                last_buy_hour = hour

        elif (hour, day) in potential_sell_hours or (highest_buy_price and price > highest_buy_price + min_profit_threshold):
            # Optimal and opportunistic selling
            selling_price = price
            profit_threshold = highest_buy_price + min_profit_threshold
            if selling_price > profit_threshold and last_buy_hour != hour:
                discharge_amount_kwh = min(charging_speed_kwh, battery_kwh - battery_capacity * min_battery)
                battery_kwh -= discharge_amount_kwh
                battery_percentage -= discharge_amount_kwh / battery_capacity * 100  # Added
                action = 'SELL'
                
                # Calculate profit
                profit = (selling_price - highest_buy_price) * discharge_amount_kwh
                total_profit += profit

        # Append to action plan
        action_entry = {
            'hour': hour,
            'day': day,
            'electricity_price': price,
            'action': action,
            # 'selling_price': selling_price if action == 'SELL' else None,
            # 'total_cumulative_profit': total_profit if action == 'SELL' else None,
            # 'battery_percentage': battery_percentage  # Added
        }
        action_plan.append(action_entry)
        print("finished actionPlan")
    return action_plan

# Generate the optimized action plan

optimized_action_plan = optimize_action_plan(data)
print(optimized_action_plan)


# [{'hour': '00:00', 'day': '22-10-2023', 'electricity_price': 0.04015, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '01:00', 'day': '22-10-2023', 'electricity_price': 0.09569, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '02:00', 'day': '22-10-2023', 'electricity_price': 0.03036, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '03:00', 'day': '22-10-2023', 'electricity_price': 0.01861, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '04:00', 'day': '22-10-2023', 'electricity_price': 0.01563, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '05:00', 'day': '22-10-2023', 'electricity_price': 0.01835, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '06:00', 'day': '22-10-2023', 'electricity_price': 0.03432, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '07:00', 'day': '22-10-2023', 'electricity_price': 0.04001, 'action': 'BUY', 'total_cumulative_profit': None},
#  {'hour': '08:00', 'day': '22-10-2023', 'electricity_price': 0.0582, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '09:00', 'day': '22-10-2023', 'electricity_price': 0.09931, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '10:00', 'day': '22-10-2023', 'electricity_price': 0.11459, 'action': 'SELL', 'total_cumulative_profit': 2.9776000000000002},
#  {'hour': '11:00', 'day': '22-10-2023', 'electricity_price': 0.14893, 'action': 'SELL', 'total_cumulative_profit': 7.328800000000001},
#  {'hour': '12:00', 'day': '22-10-2023', 'electricity_price': 0.0767, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '13:00', 'day': '22-10-2023', 'electricity_price': 0.09955, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '14:00', 'day': '22-10-2023', 'electricity_price': 0.14893, 'action': 'SELL', 'total_cumulative_profit': 11.680000000000001},
#  {'hour': '15:00', 'day': '22-10-2023', 'electricity_price': 0.07542, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '16:00', 'day': '22-10-2023', 'electricity_price': 0.08137, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '17:00', 'day': '22-10-2023', 'electricity_price': 0.09574, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '18:00', 'day': '22-10-2023', 'electricity_price': 0.12441, 'action': 'SELL', 'total_cumulative_profit': 15.050400000000002},
#  {'hour': '19:00', 'day': '22-10-2023', 'electricity_price': 0.13551, 'action': 'SELL', 'total_cumulative_profit': 15.050400000000002},
#  {'hour': '20:00', 'day': '22-10-2023', 'electricity_price': 0.13894, 'action': 'SELL', 'total_cumulative_profit': 15.050400000000002},
#  {'hour': '21:00', 'day': '22-10-2023', 'electricity_price': 0.12469, 'action': 'SELL', 'total_cumulative_profit': 15.050400000000002},
#  {'hour': '22:00', 'day': '22-10-2023', 'electricity_price': 0.11247, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '23:00', 'day': '22-10-2023', 'electricity_price': 0.10218, 'action': 'HOLD', 'total_cumulative_profit': None},
#  {'hour': '00:00', 'day': '23-10-2023', 'electricity_price': 0.09569, 'action': 'HOLD', 'total_cumulative_profit': None}]


# [{'hour': '00:00', 'day': '22-10-2023', 'electricity_price': 0.04015, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 40.0},
#  {'hour': '01:00', 'day': '22-10-2023', 'electricity_price': 0.09569, 'action': 'SELL', 'selling_price': 0.09569, 'total_cumulative_profit': 2.2216, 'battery_percentage': 20.0},
#  {'hour': '02:00', 'day': '22-10-2023', 'electricity_price': 0.03036, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 40.0},
#  {'hour': '03:00', 'day': '22-10-2023', 'electricity_price': 0.01861, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 60.0},
#  {'hour': '04:00', 'day': '22-10-2023', 'electricity_price': 0.01563, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 80.0},
#  {'hour': '05:00', 'day': '22-10-2023', 'electricity_price': 0.01835, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 95.0},
#  {'hour': '06:00', 'day': '22-10-2023', 'electricity_price': 0.03432, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 95.0},
#  {'hour': '07:00', 'day': '22-10-2023', 'electricity_price': 0.04001, 'action': 'BUY', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 95.0},
#  {'hour': '08:00', 'day': '22-10-2023', 'electricity_price': 0.0582, 'action': 'HOLD', 'selling_price': None, 'total_cumulative_profit': None, 'battery_percentage': 95.0},
#  {'hour': '09:00', 'day': '22-10-2023', 'electricity_price': 0.09931, 'action': 'SELL', 'selling_price': 0.09931, 'total_cumulative_profit': 4.588, 'battery_percentage': 75.0},
#  {'hour': '10:00', 'day': '22-10-2023', 'electricity_price': 0.11459, 'action': 'SELL', 'selling_price': 0.11459, 'total_cumulative_profit': 7.5656, 'battery_percentage': 55.0},
#  {'hour': '11:00', 'day': '22-10-2023', 'electricity_price': 0.14893, 'action': 'SELL', 'selling_price': 0.14893, 'total_cumulative_profit': 11.9168, 'battery_percentage': 35.00000000000001},
#  {'hour': '12:00', 'day': '22-10-2023', 'electricity_price': 0.0767, 'action': 'SELL', 'selling_price': 0.0767, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '13:00', 'day': '22-10-2023', 'electricity_price': 0.09955, 'action': 'SELL', 'selling_price': 0.09955, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '14:00', 'day': '22-10-2023', 'electricity_price': 0.14893, 'action': 'SELL', 'selling_price': 0.14893, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '15:00', 'day': '22-10-2023', 'electricity_price': 0.07542, 'action': 'SELL', 'selling_price': 0.07542, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '16:00', 'day': '22-10-2023', 'electricity_price': 0.08137, 'action': 'SELL', 'selling_price': 0.08137, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '17:00', 'day': '22-10-2023', 'electricity_price': 0.09574, 'action': 'SELL', 'selling_price': 0.09574, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '18:00', 'day': '22-10-2023', 'electricity_price': 0.12441, 'action': 'SELL', 'selling_price': 0.12441, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '19:00', 'day': '22-10-2023', 'electricity_price': 0.13551, 'action': 'SELL', 'selling_price': 0.13551, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '20:00', 'day': '22-10-2023', 'electricity_price': 0.13894, 'action': 'SELL', 'selling_price': 0.13894, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '21:00', 'day': '22-10-2023', 'electricity_price': 0.12469, 'action': 'SELL', 'selling_price': 0.12469, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '22:00', 'day': '22-10-2023', 'electricity_price': 0.11247, 'action': 'SELL', 'selling_price': 0.11247, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '23:00', 'day': '22-10-2023', 'electricity_price': 0.10218, 'action': 'SELL', 'selling_price': 0.10218, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0},
#  {'hour': '00:00', 'day': '23-10-2023', 'electricity_price': 0.09569, 'action': 'SELL', 'selling_price': 0.09569, 'total_cumulative_profit': 13.3788, 'battery_percentage': 15.0}]