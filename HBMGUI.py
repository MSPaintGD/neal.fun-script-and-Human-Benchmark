from tkinter import *
import pyperclip

root = Tk()
root.title("Human Benchmark GUI")
root.geometry("700x700")
root.configure(bg="#add8e6")

title_label = Label(root, text="Human Benchmark Scripts", font=("Raleway", 20, "bold"), pady=10, bg="#ffffff")
title_label.pack()

def create_section(frame, title, copy_func):
    section = Frame(frame, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
    section.pack(pady=10, fill="x", padx=30)

    label = Label(section, text=title, font=("Raleway", 14), anchor="w", bg="#ffffff")
    label.pack(side="left", expand=True, fill="x")

    button = Button(section, text="Copy", command=copy_func, font=("Raleway", 12), width=10)
    button.pack(side="right")

text_to_copy = """setInterval(() => {
    let down = new MouseEvent("mousedown", {bubbles: true, cancelable: true});
    document.getElementsByClassName("css-q4kt6s e6yfngs1")[0].dispatchEvent(down);
})"""

def copy_code():
    pyperclip.copy(text_to_copy)

create_section(root, "Aim Trainer", copy_code)

text_to_cope = """document.getElementsByClassName("letters") [0].children.forEach((char) => {
    let e = new KeyboardEvent("keydown", {
       bubbles: true,
        cancelable: true,
        key: char.innerText,
    });
    document.getElementsByClassName("letters")
[0].dispatchEvent(e);
})"""

def copy_code():
    pyperclip.copy(text_to_cope)

create_section(root, "Typing Test", copy_code)

text_to_copey = """setInterval(() => {
    document.getElementsByClassName("css-de05nr e19owgy710")[0]?.click();
[...document.querySelectorAll("[data-cellnumber]")]
    .sort((a, b) => a.dataset.cellnumber - b.dataset.cellnumber)
    .forEach((cell) => cell.click())
});"""

def copy_code():
    pyperclip.copy(text_to_copey)

create_section(root, "Chimp Test", copy_code)

text_to_coper = """let waitTime = 0; // Adjust if going too fast
const buttons = document.querySelectorAll('.css-de05nr.e19owgy710');

buttons.forEach(button => {
    const text = button.textContent.trim().toUpperCase();
    if (text === 'SEEN') button.id = 'seen';
    else if (text === 'NEW') button.id = 'new';
});

let words = [];
let shouldStop = false;

function loopWords() {
    if (shouldStop) return;
    
    const currentWord = document.querySelector('.word').textContent;

    if (words.includes(currentWord)) {
        document.getElementById('seen').click();
    } else {
        document.getElementById('new').click();
        words.push(currentWord);
    }
}

let intervalID = setInterval(loopWords, waitTime);

function stopLoop() {
    shouldStop = true;
    clearInterval(intervalID);
}"""

def copy_code():
    pyperclip.copy(text_to_coper)

create_section(root, "Verbal Memory", copy_code)

text_to_coperr = """setInterval(() => {
    let down = new MouseEvent("mousedown", { bubbles: true, cancelable: true })
    document.getElementsByClassName("view-go")
[0]?.dispatchEvent(down);
})
"""

def copy_code():
    pyperclip.copy(text_to_coperr)

create_section(root, "Reaction Test", copy_code)

text_to_copera = """const monitorTiles = async () => {
  const gridSelector = '.css-1qvtbrk.e19owgy78 .squares';
  const flippedClass = 'active';
  let previousState = null;
  let flippedTiles = [];
  let intervalId = null;

  const getGridState = () => {
    const gridContainer = document.querySelector(gridSelector);
    if (!gridContainer) return null;
    return Array.from(gridContainer.children).map(row =>
      Array.from(row.children).map(tile => tile.classList.contains(flippedClass))
    );
  };

  const clickTile = (rowIndex, colIndex) => {
    const targetTile = document.querySelector(`${gridSelector} > :nth-child(${rowIndex + 1}) > :nth-child(${colIndex + 1})`);
    if (targetTile) {
      ['mousedown', 'mouseup', 'click'].forEach(type =>
        targetTile.dispatchEvent(new MouseEvent(type, { bubbles: true, cancelable: true })));
    }
  };

  const monitorGrid = async () => {
    intervalId = setInterval(() => {
      const gridState = getGridState();
      if (!gridState) return;

      if (previousState && JSON.stringify(gridState) !== JSON.stringify(previousState)) {
        const isBoardEmpty = gridState.every(row => row.every(tile => !tile));

        if (isBoardEmpty) {
          flippedTiles.forEach(tile => clickTile(tile.rowIndex, tile.colIndex));
          flippedTiles = [];
        } else {
          gridState.forEach((row, rowIndex) =>
            row.forEach((tile, colIndex) => {
              if (tile) flippedTiles.push({ rowIndex, colIndex });
            })
          );
        }
      }

      previousState = gridState;
    }, 500);
  };

  const stopLoop = () => {
    if (intervalId) {
      clearInterval(intervalId);
    }
  };

  monitorGrid();
};

monitorTiles();"""

def copy_code():
    pyperclip.copy(text_to_copera)

create_section(root, "Sequence Memory", copy_code)

text_to_coperraa = """const monitorTiles = async () => {
  const gridSelector = '.css-hvbk5q.eut2yre0';
  const tileSelector = '.css-lxtdud.eut2yre1';
  const flippedClass = 'active';
  let initialState = null;
  let gridChangedOnce = false;
  let flippedTiles = [];
  let intervalID, emptyIntervalID;

  const getGridState = () => {
    const gridContainer = document.querySelector(gridSelector);
    if (!gridContainer) return null;

    const rows = Array.from(gridContainer.children);
    return rows.map(row => Array.from(row.children).map(tile => tile.classList.contains(flippedClass)));
  };

  const clickTile = (rowIndex, colIndex) => {
    const gridContainer = document.querySelector(gridSelector);
    const targetTile = gridContainer?.children[rowIndex]?.children[colIndex];
    if (targetTile) {
      ['mousedown', 'mouseup', 'click'].forEach(type =>
        targetTile.dispatchEvent(new MouseEvent(type, { bubbles: true, cancelable: true })));
    }
  };

  const monitorGrid = async () => {
    intervalID = setInterval(() => {
      const gridState = getGridState();
      if (!gridState) return;

      if (!initialState) {
        initialState = gridState;
        return;
      }

      const isGridChanged = !gridState.every((row, rowIndex) =>
        row.every((tile, colIndex) => tile === initialState[rowIndex][colIndex])
      );

      if (!gridChangedOnce && isGridChanged) {
        gridChangedOnce = true;
        flippedTiles = gridState.reduce((tiles, row, rowIndex) => {
          row.forEach((tile, colIndex) => {
            if (tile) tiles.push({ rowIndex, colIndex });
          });
          return tiles;
        }, []);
        return;
      }

      if (gridChangedOnce && isGridChanged) {
        clearInterval(intervalID);
        setTimeout(() => {
          flippedTiles.forEach(tile => clickTile(tile.rowIndex, tile.colIndex));
          setTimeout(() => {
            monitorEmptyBoard();
          }, 500);
        }, 1500);
      }
    }, 500);
  };

  const monitorEmptyBoard = async () => {
    emptyIntervalID = setInterval(() => {
      const gridState = getGridState();
      if (!gridState) return;

      const isEmpty = gridState.every(row => row.every(tile => !tile));

      if (isEmpty) {
        clearInterval(emptyIntervalID);
        initialState = null;
        gridChangedOnce = false;
        monitorGrid();
      }
    }, 500);
  };

  monitorGrid();
};

monitorTiles();"""

def copy_code():
    pyperclip.copy(text_to_coperraa)

create_section(root, "Visual Memory", copy_code)

text_to_coperra = """let prevNumber = '';
let intervalID;

const copyNumberToClipboard = () => {
    const bigNumberElement = document.querySelector('.big-number');
    const number = bigNumberElement?.textContent.trim();

    if (number) {
        navigator.clipboard.writeText(number)
            .then(() => console.log('Number copied to clipboard:', number))
            .catch((error) => console.error('Error copying number:', error));
    }
};

const processNumber = () => {
    intervalID = setInterval(() => {
        const bigNumberElement = document.querySelector('.big-number');
        const number = bigNumberElement?.textContent.trim();

        if (number && number !== prevNumber) {
            copyNumberToClipboard();
            prevNumber = number;
        }
    }, 1000);
};

const stopLoop = () => {
    clearInterval(intervalID);
};

processNumber();"""

def copy_code():
    pyperclip.copy(text_to_coperra)

create_section(root, "Number Memory", copy_code)

root.mainloop()