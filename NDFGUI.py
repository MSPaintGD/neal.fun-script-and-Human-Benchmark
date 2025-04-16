from tkinter import *
import pyperclip

root = Tk()
root.title("Neal.fun GUI")
root.geometry("700x700")
root.configure(bg="#add8e6")

title_label = Label(root, text="NDFGUI", font=("Raleway", 20, "bold"), pady=10, bg="#ffffff")
title_label.pack()

def create_section(frame, title, copy_func):
    section = Frame(frame, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
    section.pack(pady=10, fill="x", padx=30)

    label = Label(section, text=title, font=("Raleway", 14), anchor="w", bg="#ffffff")
    label.pack(side="left", expand=True, fill="x")

    button = Button(section, text="Copy", command=copy_func, font=("Raleway", 12), width=10)
    button.pack(side="right")

text_to_copy = """(function() {
    let s = document.querySelector("main svg").getBoundingClientRect(),
        cx = s.width / 2 + s.x,
        cy = s.height / 2 + s.y,
        r = s.width / 3,
        d = document.querySelector("main div"),
        a = 0;
    for (let e = 0; e < 50; e++) {
        a += Math.acos(1 - Math.pow(60 / r, 2) / 2);
        let t = Math.round(cx + r * Math.cos(a)),
            n = Math.round(cy + r * Math.sin(a));
        if (0 === e && d.dispatchEvent(new MouseEvent("mousedown", { clientX: t, clientY: n })),
            d.dispatchEvent(new MouseEvent("mousemove", { clientX: t, clientY: n })));
    }
    d.dispatchEvent(new MouseEvent("mouseup"));
})();"""

def copy_code():
    pyperclip.copy(text_to_copy)

create_section(root, "Perfect Circle", copy_code)

text_to_copy2 = """(function() {
    console.log("Auto Clicker and Auto Upgrader started!");

    const clickInterval = 20; // 1 = 1ms ( lower u go faster it goes! )
    const upgradeInterval = 1000; // Checks upgrades every second. 1000ms = 1s ( lower u go faster it goes! )

    function autoClick() {
        const mainButton = document.querySelector(".main-btn"); // Update selector if necessary
        if (mainButton) {
            mainButton.click();
        }
    }

    function autoUpgrade() {
        const upgrades = document.querySelectorAll(".upgrade"); // Update selector if necessary
        upgrades.forEach((upgrade) => {
            if (!upgrade.classList.contains("disabled")) {
                upgrade.click();
            }
        });
    }

    
    const clicker = setInterval(autoClick, clickInterval);

    
    const upgrader = setInterval(autoUpgrade, upgradeInterval);

   
    window.stopAutomation = function() {
        clearInterval(clicker);
        clearInterval(upgrader);
        console.log("Auto Clicker and Auto Upgrader stopped!");
    };

    console.log("You can stop me by typing (stopAutomation) in the console.");
})();"""

def copy_code():
    pyperclip.copy(text_to_copy2)
create_section(root, "Stimulation Clicker", copy_code)

text_to_copy3 = """
let lastClearButtonClick = 0;
const DRAG_STEPS = 10;
const CLEAR_BUTTON_DELAY = 5500;
const THREAD_COUNT = 8;
const TARGET_COORDINATES = [
    { x: 300, y: 300 },
];

const OFFSET_VALUES = [
    { x: 50, y: 50 }, 
    { x: 100, y: 100 },
    { x: 150, y: 150 },
    { x: 200, y: 200 },
];

function simulateDragAndDrop(element, startX, startY, targetX, targetY, steps = DRAG_STEPS) {
    function triggerMouseEvent(target, eventType, clientX, clientY) {
        const event = new MouseEvent(eventType, {
            bubbles: true,
            cancelable: true,
            clientX,
            clientY,
            view: window,
        });
        target.dispatchEvent(event);
    }

    console.log(`Dragging from (${startX}, ${startY}) to (${targetX}, ${targetY})`);

    triggerMouseEvent(element, "mousedown", startX, startY);

    const deltaX = (targetX - startX) / steps;
    const deltaY = (targetY - startY) / steps;
    let currentX = startX;
    let currentY = startY;

    return new Promise((resolve) => {
        function moveMouse() {
            currentX += deltaX;
            currentY += deltaY;

            triggerMouseEvent(document, "mousemove", currentX, currentY);

            if (Math.abs(currentX - targetX) < Math.abs(deltaX) && Math.abs(currentY - targetY) < Math.abs(deltaY)) {
                triggerMouseEvent(document, "mouseup", targetX, targetY);
                console.log("Drag-and-drop completed.");

                element.style.position = "absolute";
                element.style.left = `${targetX}px`;
                element.style.top = `${targetY}px`;

                resolve();
            } else {
                requestAnimationFrame(moveMouse);
            }
        }
        requestAnimationFrame(moveMouse);
    });
}

function saveProcessedPairs(processedPairs) {
    localStorage.setItem("processedPairs", JSON.stringify([...processedPairs]));
}

async function clickClearButtonNonBlocking() {
    const clearBtn = document.querySelector(".clear");
    if (clearBtn) {
        const now = Date.now();
        if (now - lastClearButtonClick < CLEAR_BUTTON_DELAY) {
            console.log("Clear button click throttled.");
            return;
        }

        console.log("Waiting before clicking the clear button...");
        lastClearButtonClick = now;
        setTimeout(() => {
            clearBtn.click();
            console.log("Clear button clicked.");
        }, CLEAR_BUTTON_DELAY);
    } else {
        console.warn("Clear button not found.");
    }
}

async function processCombination(firstItem, secondItem, target1X, target1Y, target2X, target2Y, offsetIndex) {
    const firstRect = firstItem.getBoundingClientRect();
    const secondRect = secondItem.getBoundingClientRect();

    const firstStartX = firstRect.x + firstRect.width / 2;
    const firstStartY = firstRect.y + firstRect.height / 2;
    const secondStartX = secondRect.x + secondRect.width / 2;
    const secondStartY = secondRect.y + secondRect.height / 2;

    const offset = OFFSET_VALUES[offsetIndex];

    await simulateDragAndDrop(firstItem, firstStartX, firstStartY, target1X + offset.x, target1Y + offset.y);
    await simulateDragAndDrop(secondItem, secondStartX, secondStartY, target2X + offset.x, target2Y + offset.y);
    await clickClearButtonNonBlocking();
}

async function processItems(itemsRow, processedPairs, threadIndex) {
    const items = [...itemsRow.getElementsByClassName("item")];
    console.log(`Found ${items.length} items in row.`);

    const target = TARGET_COORDINATES[threadIndex]; 

    let offsetIndex = 0;
    for (let i = 0; i < items.length; i++) {
        for (let j = i + 1; j < items.length; j++) {
            const pairKey = `${i}-${j}`;
            if (!processedPairs.has(pairKey)) {
                processedPairs.add(pairKey);
                saveProcessedPairs(processedPairs);

                console.log(`Processing combination: ${pairKey}`);

                await processCombination(
                    items[i], 
                    items[j], 
                    target.x, 
                    target.y, 
                    target.x, 
                    target.y,
                    offsetIndex
                );

                offsetIndex = (offsetIndex + 1) % OFFSET_VALUES.length;
            }
        }
    }
}

async function processThread(threadIndex, itemsRows, processedPairs) {
    const rowSubset = itemsRows.filter((_, index) => index % THREAD_COUNT === threadIndex);

    for (const row of rowSubset) {
        console.log(`Thread ${threadIndex}: Processing row:`, row);
        await processItems(row, processedPairs, threadIndex); 
    }
    console.log(`Thread ${threadIndex}: Processing completed.`);
}

async function Run() {
    const processedPairs = new Set(JSON.parse(localStorage.getItem("processedPairs") || "[]"));
    const itemsRows = [...document.querySelectorAll(".items-inner")];
    console.log(`Found ${itemsRows.length} item rows.`);

    const threadPromises = Array.from({ length: THREAD_COUNT }, (_, index) =>
        processThread(index, itemsRows, processedPairs)
    );

    await Promise.all(threadPromises);
    console.log("All threads completed.");
}

Run().catch((error) => console.error("An error occurred during the Run:", error));"""

def copy_code():
    pyperclip.copy(text_to_copy3)
create_section(root, "Infinite Craft", copy_code)

text_to_copy4 = """// Find the speed slider - usually the second range input on the page
const sliders = document.querySelectorAll('input[type="range"]');
const speedSlider = sliders[1]; // Index might vary, but usually speed is the second one

// Update max value to a huge number
speedSlider.max = '999999999999999999999999999999999999999';

// Optional: Update step for smoother control (smaller = slower movement)
speedSlider.step = '1';

// Optional: Reset current value if needed
speedSlider.value = '1000000000000000000000';

// Optional: Update the visual style if it uses CSS custom properties
const min = parseFloat(speedSlider.min);
const max = parseFloat(speedSlider.max);
const value = parseFloat(speedSlider.value);
const percent = ((value - min) / (max - min)) * 100;
speedSlider.style.setProperty('--percent', `${percent}%`);
speedSlider.style.setProperty('--offset', `0px`);

console.log("Speed slider updated 🚀");"""


def copy_code():
    pyperclip.copy(text_to_copy4)

create_section(root, "Asteroid Launcher Speed", copy_code)

text_to_copy5 = """// Select the specific slider (adjust selector if needed)
const slider = document.querySelector('input[type="range"]');

// Update the max value to a huge number
slider.max = '99999999999999999999999999999999999999';

// Optional: Recalculate and update the --percent and --offset styles (basic example)
const min = parseFloat(slider.min);
const max = parseFloat(slider.max);
const value = parseFloat(slider.value);

// Compute new percent
const percent = ((value - min) / (max - min)) * 100;
slider.style.setProperty('--percent', `${percent}%`);

// Optional: reset offset if needed
slider.style.setProperty('--offset', `0px`);"""


def copy_code():
    pyperclip.copy(text_to_copy5)

create_section(root, "Asteroid Launcher Diameter", copy_code)

text_to_copy6 = """const target = document.querySelector('button'); // or whatever the clickable is

// Start 5 simultaneous clickers
for (let i = 0; i < 5; i++) {
  setInterval(() => target.click(), 1); // each one clicks every 1ms
}"""


def copy_code():
    pyperclip.copy(text_to_copy6)

create_section(root, "Sun VS Moon (Sun, cant find a way to make it moon)", copy_code)

root.mainloop()