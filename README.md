# PythonXSQLite

**PythonXSQLite** is a lightweight and user-friendly command-line application for managing your favorite YouTube videos. Built with Python and SQLite, it offers an easy way to add, update, list, and delete video entries stored locally in a robust database.

---

## Features

- **List** all saved favorite YouTube videos with their details  
- **Add** new videos with name and duration  
- **Update** existing videos by ID  
- **Delete** videos by ID  
- **Simple and intuitive command-line interface**  
- Uses **SQLite** for reliable and persistent local storage  

---

## Getting Started

### Prerequisites

- Python 3.6 or higher (comes with SQLite bundled)

### Installation

1. **Clone the repository or download the script:**
    ```
    git clone https://github.com/yourusername/PythonXSQLite.git
    cd PythonXSQLite
    ```
2. **Run the application:**
    ```
    python youtube_favorites_manager.py
    ```

---

## Usage

When you run the program, you’ll see a menu:

🎬 YouTube Manager Application

1️⃣ List All Favorite Videos
2️⃣ Add a YouTube Video
3️⃣ Update a YouTube Video
4️⃣ Delete a YouTube Video
5️⃣ Exit

Enter your choice (1-5):


- Select the corresponding number to perform an action.
- Follow prompts to add, update, or delete videos by their ID.
- Videos are saved persistently in a local SQLite database (`youtube_videos.db`).

---

## Code Structure

- **youtube_favorites_manager.py** — Main program handling user interaction and database operations.
- SQLite database file: **youtube_videos.db** (auto-created on first run)

---

## Contributing

Contributions are welcome!  
Please fork the repository and submit a pull request with your improvements or bug fixes.

---

## License

This project is licensed under the **MIT License**.  
See the [`LICENSE`](LICENSE) file for details.

---

## Contact

For questions or support, please contact:

- **Your Name** — your.email@example.com  
- **GitHub:** [https://github.com/yourusername](https://github.com/yourusername)

---

*Made with ❤️ for easy and effective YouTube video management.*
