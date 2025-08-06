import sqlite3

# Establishing database connection
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Creating table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
conn.commit()


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("\n📂 No videos found in your favorites!\n")
        return

    print("\n📺 Favorite YouTube Videos:")
    print("-" * 40)
    for video in videos:
        print(f"🎬 ID: {video[0]} | Name: {video[1]} | Duration: {video[2]}")
    print("-" * 40 + "\n")


def add_video(name, time):
    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("✅ Video added successfully!\n")


def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",
                   (new_name, new_time, video_id))
    if cursor.rowcount == 0:
        print("❌ No video found with the given ID.\n")
    else:
        conn.commit()
        print("✅ Video updated successfully!\n")


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    if cursor.rowcount == 0:
        print("❌ No video found with the given ID.\n")
    else:
        conn.commit()
        print("🗑️ Video deleted successfully!\n")


def main():
    while True:
        print("\n🎬 YouTube Manager Application")
        print("=" * 35)
        print("1️⃣  List All Favorite Videos")
        print("2️⃣  Add a YouTube Video")
        print("3️⃣  Update a YouTube Video")
        print("4️⃣  Delete a YouTube Video")
        print("5️⃣  Exit")
        print("=" * 35)

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
            continue

        if choice == 1:
            list_all_videos()
        elif choice == 2:
            name = input("🎥 Enter the video name: ").strip()
            time = input("⏱️  Enter the video duration: ").strip()
            if name and time:
                add_video(name, time)
            else:
                print("⚠️  Name and time cannot be empty.\n")
        elif choice == 3:
            try:
                video_id = int(input("🔁 Enter the video ID to update: "))
                new_name = input("🎥 New video name: ").strip()
                new_time = input("⏱️  New video duration: ").strip()
                if new_name and new_time:
                    update_video(video_id, new_name, new_time)
                else:
                    print("⚠️  Name and time cannot be empty.\n")
            except ValueError:
                print("⚠️  Invalid ID. Please enter a numeric value.\n")
        elif choice == 4:
            try:
                video_id = int(input("🗑️ Enter the video ID to delete: "))
                delete_video(video_id)
            except ValueError:
                print("⚠️  Invalid ID. Please enter a numeric value.\n")
        elif choice == 5:
            print("👋 Exiting the application. Goodbye!")
            break
        else:
            print("⚠️  Invalid choice! Please select from 1 to 5.\n")


if __name__ == '__main__':
    main()
    conn.close()
