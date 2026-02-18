import streamlit as st

books = []

# --------- APP TITLE ---------
st.title("📚 Book Checker App")
st.write("Enter a book title to check if it exists in the database.")

# --------- USER INPUT ---------
user_input = st.text_input("Book Title")

# --------- CHECK BUTTON ---------
if st.button("Check Book"):
    if user_input.strip() == "":
        st.warning("Please enter a book title.")
    elif user_input in books:
        st.success("The book exists in the database!")
    else:
        st.error("The book is NOT in the database.")

# Полета за въвеждане
title = st.text_input("Заглавие")
author = st.text_input("Автор")

# Бутон за добавяне
if st.button("Добави книга"):
    books.append(title)
    st.success("Книгата е добавена!")

# Показване на книгите
st.write("### Списък с книги:")
st.write(books)
