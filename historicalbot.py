import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

points={}
questions={}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('start'):
        await message.channel.send("Начнём нашу историческую викторину!")
        await message.channel.send('''В каком году образовалось Древнерусское государство? 
А: 882
Б: 862
В: 998''')
        points [message.author]=0
        questions [message.author]=0
        return
    
    if message.content in ['А', 'Б', 'В']:
        if questions [message.author]==0:
            if message.content=='А':
                points [message.author]+=1
            if message.content=='Б':
                points [message.author]+=0
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Личное войско Ивана Грозного? 
А: Стрельцы
Б: Бояре
В: Опричники''')
            return

        if questions [message.author]==1:
            if message.content=='А':
                points [message.author]+=0
            if message.content=='Б':
                points [message.author]+=0
            if message.content=='В':
                points [message.author]+=1
            questions [message.author]+=1
            await message.channel.send('''Какую войну историки называют Нулевой Мировой?
А: Крымскую
Б: Отечественнуб войну 1812 года
В: Русско-персидскую''')
            return
        

        if questions [message.author]==2:
            if message.content=='А':
                points [message.author]+=1
            if message.content=='Б':
                points [message.author]+=0
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Какой русский император был рыцарем Мальтийского ордена?
А: Николай 1
Б: Павел 1
В: Алекандр 1''')
            return
        
        if questions [message.author]==3:
            if message.content=='А':
                points [message.author]+=0
            if message.content=='Б':
                points [message.author]+=1
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Кто провёл военную реформу, установившую систему несения воинской повинности, которая используется до сих пор? 
А: Победоносцев
Б: Милютин
В: Сперанский''')
            return
    
        if questions [message.author]==4:
            if message.content=='А':
                points [message.author]+=0
            if message.content=='Б':
                points [message.author]+=1
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Сколько декабристов было казнено в результате восстания?
А: 7
Б: 5
В: 3''')
            return

        if questions [message.author]==5:
            if message.content=='А':
                points [message.author]+=0
            if message.content=='Б':
                points [message.author]+=1
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Как умер Александр 2?
А: Был зарезан на улице
Б: Был взорван террористами
В: Был задушен в собственном замке''')
            return
    
        if questions [message.author]==6:
            if message.content=='А':
                points [message.author]+=0
            if message.content=='Б':
                points [message.author]+=1
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Какое название получила поездка Петра 1 в Европу в 1697-1698 г.г.? 
А: Дипломатическая миссия
Б: Открытие окна в Европу
В: Великое посольство''')
            return
   
        if questions [message.author]==7:
            if message.content=='А':
                points [message.author]+=0
            if message.content=='Б':
                points [message.author]+=0
            if message.content=='В':
                points [message.author]+=1
            questions [message.author]+=1
            await message.channel.send('''Какой элемент одежды появился во время Крымской войны? 
А: Кардиган
Б: Шинель
В: Берцы''')
            return
        
        if questions [message.author]==8:
            if message.content=='А':
                points [message.author]+=1
            if message.content=='Б':
                points [message.author]+=0
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1
            await message.channel.send('''Сколько в нашей стране было правящих династий?
А: 3
Б: 2
В: 5''')
            return

        if questions [message.author]==9:
            if message.content=='А':
                points [message.author]+=1
            if message.content=='Б':
                points [message.author]+=0
            if message.content=='В':
                points [message.author]+=0
            questions [message.author]+=1

    if questions [message.author]==10:
        if points [message.author]==0:
            await message.channel.send("К сожалению, вы ни на один вопрос не ответили правильно. Ваш результат: 0/10. Вам следует уделять больше внимания Истории!")

        if points [message.author]==1:
            await message.channel.send("Ваш результат: 1/10. Вам следует уделять больше времени изучению Истории!")
        
        if points [message.author]==2:
            await message.channel.send("Ваш результат: 2/10. Вам следует уделять больше времени изучению Истории!")

        if points [message.author]==3:
            await message.channel.send("Ваш результат: 3/10. Вам следует уделять больше времени изучению Истории!")
        
        if points [message.author]==4:
            await message.channel.send("Ваш результат: 4/10! Неплохо, но Вам стоит подучить Историю!")

        if points [message.author]==5:
            await message.channel.send("Ваш результат: 5/10. Неплохо, но Вам следует уделять больше времени изучению Истории")

        if points [message.author]==6:
            await message.channel.send("Ваш результат: 6/10. Хорошо, но есть куда стремиться!")

        if points [message.author]==7:
            await message.channel.send("Ваш результат: 7/10. Хорошо, но есть куда стремиться!")

        if points [message.author]==8:
            await message.channel.send("Ваш результат: 8/10. Очень хорошо, но есть куда стремиться!")

        if points [message.author]==9:
            await message.channel.send("Ваш результат: 9/10. Отлично, Вы хорошо знаете историю России!")

        if points [message.author]==10:
            await message.channel.send("Ваш результат: 10/10. Отлично, Вы очень хорошо знаете историю России!")

client.run("MTI2NDg3MzM3NjI1NDY1NjU0Mg.GurSYn.S6rMfrfBgxmsklJDUPBG9Zy2RkukahWT7YWPjk")
