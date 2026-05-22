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
5. Explore the city

Time Slots:
- Morning
- Afternoon
- Evening
- Night

The demo ends after 14 in-game days.
At the end of Day 14, the game evaluates the player’s money, mood, reputation, and relationships to determine the ending.
Day 1 - Morning

The city comes alive in an orchestra of horns honking and trains rumbling. You don't even need your alarm; you're awake too.

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
5. Explore the city

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

Money - Tracks how much income the player has. Can be used for rent, coffee, events, and relationships.

Energy - Tracks how tired the player is. Work, errands, and events lower energy, while coffee and rest restore it.

Mood - Tracks the player’s emotional wellbeing. Rest, fun, and social choices improve mood. Stressful work or bad events lower it.

Reputation - Tracks the player’s capability at work and in the city. Decisions affect this both negatively and positively.

Day - Tracks the current day in the 14-day demo period.

Time Slot - Tracks whether it is morning, afternoon, or evening.

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
Reputation: -100 minimum, 100 maximum
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

Explore the City:
Money -25
Energy -15
Mood +20

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
The Burnout Ending

If relationships are high:
The Neighborhood Hero Ending

If mood and relationships are high:
The Talk of the City Ending

If money is too low:
The Eviction Notice Ending

If reputation is high:
The Overachiever Ending

## Locations

Apartment:
A home base where the player can rest, journal, check stats, and eventually save the game. Fun fact: it's an overpriced studio.

Coffee Shop:
A social location where the player can buy coffee, meet people, and hear city rumors.

Temp Agency:
A work location where the player can take shifts, earn money, and build reputation. There is a watercooler.

Bookstore:
A creative/social location where the player can browse, attend beat poetry, and meet literary NPCs.

Park/Subway Station:
A public city location where the player can walk, decompress, encounter strangers, and trigger random events.

Music Venue:
A nightlife/culture location where the player can go to concerts, boost mood, lose energy, and experience city life.

Restaurant:
Optional/Future location. An overpriced steakhouse in a rich neighborhood. Fills energy completely but drains half your wallet.

## NPCs

Greta Green:
A friendly punk rocker who you can meet at concerts or on the subway. 

Norma: 
A happy-go-lucky widow who hangs out at the coffee shop a couple times a week. She drinks tea and gives advice.

Lou Luxe:
A stock broker who lives in a penthouse. He's arrogant and likes fancy things. He can be met at the restaurant.

## What Version 1 Includes

## Future Features

## Future Features

- Night time slot for concerts, nightlife, and late-night city events

## One Sentence Summary - Big City is a text-based Python life sim where the player has fourteen days to build a stable life in a new city by balancing money, energy, mood, work reputation, and relationships.