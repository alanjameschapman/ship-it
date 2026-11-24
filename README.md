# Ship It!

## Goal

A terminal reaction game anyone can download and play, that we can keep improving without breaking it.

## Audience

One player, at their own terminal, with a minute to spare.

## In scope

The game itself. Remembering your best time while you play.

## Out of scope

Online leaderboards. Player accounts. Remembering your best time between sessions. Phones and tablets.

## Team

- Priya: decides what we build (Product Owner)
- Alan: builds it (Developer) and keeps it running (Ops)
- Sam: checks it works (QA)

## Design

### Flow

1. Show the welcome message and how to play
2. Ask "Ready?" (q goes to 7)
3. Lights: RED, AMBER, GREEN, a random wait before each
4. Pressed before green? False start, back to 2
5. Show the time: a new best, or the best so far
6. Back to 2
7. Say goodbye

### Parts

- `play_round()` runs the lights and returns the time, or a false start
- `pressed_enter()` waits, and notices an early press
- `is_new_best()` decides if a time beats the best so far
- `main()` the flow itself

### Alternatives considered

One function that does everything. Rejected: nobody could check the best-time rule without playing a round, and every change would mean reading all of it.

### How we'll check it

Play it: a round, a false start, a faster round, a slower round, q. One automated test for the best-time rule, run with one command (requirement 11).

### Where it runs

Any laptop with Python 3 and colorama, for now. Later, a container, so a new player needs only Docker (requirement 13).
