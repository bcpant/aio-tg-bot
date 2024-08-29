def reply_message_default(correct_answer, lives):
    answer = (
        f'Вы ошиблись, верный перевод: {correct_answer}\n'
        f'Осталось {lives} ❤️\n'
    )
    return answer

def  game_over_msg_rec(guessed_words): 
    answer = (
        f'Игра окончена.\n'
        f'Слов отгадано: {guessed_words}\n'
        f'Поздравляю! Вы установили новый рекорд!'
    )
    return answer

def game_over_msg(guessed_words):
    answer = (
        f'Игра окончена.\n'
        f'Слов отгадано: {guessed_words}\n'
    )
    return answer

def stats_msg(total_count, right_answers, wrong_answers, right_proc, surv_record):
    answer = (
        f'🏁*Бесконечный режим*\n'
        f'*------------------------------------*\n'
        f'🔢Слов проверено: {total_count}\n'
        f'✅Правильных ответов: {right_answers}\n'
        f'❌Неправильных ответов: {wrong_answers}\n'
        f'✍️Процент правильных ответов: {float(right_proc)}%\n'
        f'*------------------------------------*\n'
        f'🏁*Три жизни*\n' 
        f'❤️Рекорд: {surv_record}'
    )
    return answer 