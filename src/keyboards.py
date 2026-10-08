from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Python"),],
    [KeyboardButton(text="Java"),],
    [KeyboardButton(text="JavaScript"),]
  ]  )

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Документация Python", url="https://docs.python.org/3/")],
    [InlineKeyboardButton(text="Документация Java", url="https://docs.oracle.com/en/java/")],
    [InlineKeyboardButton(text="Документация JavaScript",url="https://developer.mozilla.org/en-US/docs/Web/JavaScript")],
     ]  )