# Big City Design Document

## Project Summary

## Main Goal

## Core Loop
Each day in Big City has three time slots:

1. Morning
2. Afternoon
3. Evening

During each time slot, the player chooses one activity.

After each activity:
- Player stats update
- Time moves forward
- The game shows the next time slot

After evening:
- The day ends
- A short day summary appears
- The next day begins

After Day 14:
- The game shows an ending based on the player’s stats and choices
Start Day
Show current day and stats
Morning choice
Update stats
Afternoon choice
Update stats
Evening choice
Update stats
End day summary
Advance to next day
Repeat until Day 14
Show final ending

Day: 1
Time: Morning

Money: $100
Energy: 100
Mood: 50
Reputation: 0

What would you like to do?
1. Work a shift
2. Rest at apartment
3. Visit coffee shop
4. Go to the park

Time Slots:
- Morning
- Afternoon
- Evening

The demo ends after 14 in-game days.
At the end of Day 14, the game evaluates the player’s money, mood, reputation, and relationships to determine the ending.
Day 1 - Morning

The city wakes outside your apartment window. Car horns, footsteps, and the rumble of the subway remind you that you are really here.

Stats:
Money: $100
Energy: 100
Mood: 50
Reputation: 0

Choices:
1. Take a temp shift
2. Rest a little longer
3. Visit Coffee Shop
4. Walk through the park

Player chooses: Take a temp shift

Result:
Money +65
Energy -25
Mood -5
Reputation +5

New stats:
Money: $165
Energy: 75
Mood: 45
Reputation: 5

Time advances to Afternoon.

## Player Stats

Money - tracks how much income player has. Can be used for rent, coffee, events, relationships.
Energy - Tracks how tired the player is. Work, errands, and events all lower energy while coffee and rest restore it.
Reputation - Tracks the player's capability at work and in the city as well as relationships. Decisions effect this both negatively and positively.
Day - tracks the day in the 14 day demo period
Time Slot - tracks whether it's morning, afternoon, or evening

Starting Stats:
Money: 100
Energy: 100
Mood: 50
Reputation: 0
Day: 1
Time Slot: Morning

Stat Limits:

Money: 0 minimum, no strict maximum
Energy: 0 minimum, 100 maximum
Mood: 0 minimum, 100 maximum
Reputation: 0 minimum, 100 maximum
Day: 1 minimum, 14 maximum
Time Slot: Morning, Afternoon, Evening

## Basic Action Effects
Work a shift:
Money +65
Energy -25
Mood -5
Reputation +5

Rest at apartment:
Energy +30
Mood +5

Journal:
Mood +10
Energy -5

Buy coffee:
Money -4
Energy +10
Mood +5

Talk to NPC:
Relationship +5
Energy -5
Mood +3

Walk through park:
Mood +10
Energy -5

Attend bookstore reading:
Mood +10
Energy -10
Nico relationship +5

Low Energy:
If energy is too low, the player may not be able to work or socialize.

Low Mood:
If mood is too low, the player may receive a burnout-style ending or have fewer social options.

Low Money:
If money is too low by Day 14, the player may fail to make rent.

High Reputation:
Higher reputation may unlock better work opportunities.

High Relationships:
Higher relationships may unlock friendship-based endings.

Money
Mood
Reputation
Relationships
If money is high but mood is low:
The Hustler Ending

If relationships are high:
The Local Ending

If mood and relationships are high:
The Fresh Start Ending

If money is too low:
The Barely Scraping By Ending

If reputation is high:
The Career Climber Ending

## Locations

## NPCs

## What Version 1 Includes

## Future Features

## One Sentence Summary - Big City is a text-based Python life sim where the player has fourteen days to build a stable life in a new city by balancing money, energy, mood, work reputation, and relationships.