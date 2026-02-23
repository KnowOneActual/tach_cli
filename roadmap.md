# Terminal Event Clock & Timer

## Project Description
A lightweight terminal application designed for live productions, events, and structured meetings. It provides a distraction-free timekeeping tool. The app focuses on a highly visible, auto-scaling text display that toggles seamlessly between a standard clock and a countdown timer. 

## Design Thoughts
Built using Framestorming and Musk's 5-Step Process to solve the core problem of maintaining perfect pacing without breaking focus, while aggressively avoiding feature creep.

* **Question the Frame:** The app prioritizes simple visual communication. Color shifts (Green > Yellow > Red) are used instead of multiple competing visual alerts. 
* **Delete the Unnecessary:** Complex menus, data logging, and OS-level window hacking have been removed. The terminal emulator itself will handle styling like background transparency and borderless modes.
* **Simplify and Optimize:** The core logic focuses strictly on large text that counts down, changes color, and goes negative for overtime. 

## Core Features (The Minimum Viable Product)
* Auto-scaling text that adjusts perfectly when the window is resized.
* Toggle between a countdown timer and the current time of day.
* Text changes color based on time remaining (e.g., Green to Yellow to Red).
* Overtime counter that turns red and counts into negative numbers when time expires.
* Basic keyboard controls to pause, reset, or adjust minutes.
* Quick launch via a shell alias (e.g., `event 30`).

## Nice-to-Haves (Future Phases)
* Multi-profile configurations for different meeting lengths.
* Vim-style keybindings for rapid, home-row adjustments.
* Global hotkeys to pause or adjust time even when the terminal is not the active window.

## Future Considerations (Pending User Demand)
*These features were removed to keep the initial build lean, but can be revisited if there is a strong need:*
* Subtle progress bar on the edge of the terminal.
* Gentle flashing alerts at critical time milestones.
* Built-in application-level background transparency and borderless "true minimalist" mode.

## Development Roadmap

**Phase 1: The Core Display & Toggles**
Set up the Python script using the Textual or Rich layout library. Build the logic to display the time, accept a minute input, and toggle between the clock and the timer views. Add the basic pause and reset controls.

**Phase 2: Visual Pacing & Overtime**
Introduce the time threshold logic. Add the color shifts and the red overtime count-up feature. Ensure the text auto-scales smoothly during window resizing.

**Phase 3: Advanced Controls (Optional)**
Build out the nice-to-have features like Vim-style keybindings, global hotkeys, and multi-profile loading commands.


## starting foundation:

Language: Python.

UI Framework: Textual. This library is designed specifically for building responsive terminal user interfaces. It automatically handles the complex math for window resizing and layout management so we do not have to build it from scratch.

Styling Engine: Rich. Textual uses this under the hood to manage text formatting and colors. This will make handling our green-to-yellow-to-red time shifts effortless.