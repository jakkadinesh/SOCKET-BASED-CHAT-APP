# 💬 Socket-Based Chat Application

## 📌 Overview
A simple real-time chat application built using Python sockets. It enables multiple clients to connect to a server and exchange text messages instantly. This project demonstrates how socket programming enables basic network communication between clients and servers.

---

## 🚀 Features
- 🧑‍🤝‍🧑 Multiple clients can connect to a single server
- 📨 Real-time message broadcast to all connected users
- 🔒 Server-client architecture using TCP sockets
- ⏱️ Asynchronous message handling using multithreading
- 💻 Command-line based interface

---

## 🛠️ Tech Stack
- **Language:** Python
- **Modules:** `socket`, `threading`

---

## 🧠 How It Works
- The **server** listens for incoming client connections.
- When a **client** connects, it is assigned a thread to handle its communication.
- Messages from any client are **broadcast** to all others in the chat room.
- The server runs continuously, handling multiple clients concurrently.

---

## 📁 Project Structure
