# NextTrain Israel App Tooling

A SQLite database that includes the data needed to operate the NextTrain app, an unofficial time schedule app for the
Israeli railway for Android and iPhone, and the set of tools to create this database.

## The Main Idea

The NextTrain Israel App was inspired by
reading ["About Face 3" by Alan Cooper](https://www.goodreads.com/en/book/show/289062) and designed and published in
2009 to provide users with an experience similar to being at the rail station, looking at the real schedule board. I
find this experience more straightforward and useful than having to choose the
departure and destination station and then specify the date and time.

The latest version of the official Israel Train app is now quite good and reliable (which wasn't the case 5-10 years
ago). However, some individuals, including railroad workers and conductors, still prefer NextTrain. The only issue is
that I don't have the capacity to update the database frequently enough.

Therefore, I've decided to open-source the tooling in case somebody could help me keep up with the updates.

## Current State

Currently, the repository contains the sole SQLite database with all the required data organized into two tables:

    1. ZTLSTATIONS # contains 68 stations
    2. ZTLSCHEDULE # contains 42442 records of the intersections of all trains 
                   # and the stations in the time dimention

Additionally, it contains a simple Python script that demonstrates a few queries to the database, similar to how it
works in the app.

The first function prints all stations with their corresponding station IDs in the second column.

    query_all_stations()
     
     (0, 300, 34.963202, 31.892953, 'پآتي (اطراف) موديعين', 'מודיעין - פאתי מודיעין', 'Модиин Патей', 'Modiin - Paate Modiin')
     (0, 400, 35.005708, 31.901059, 'موديعين مركز', 'מודיעין מרכז', 'Модиин центр', 'Modiin Center')
     (0, 680, 35.2014803, 31.7882125, 'أورشليم – يتسحاق ناڤون', 'ירושלים - יצחק נבון', 'Иерусалим - Ицхак Навон', 'Jerusalem - Yitzhak Navon')
     ...
     (0, 9650, 34.5701363, 31.410832, 'نتيفوت', 'נתיבות', 'Нетивот', 'Netivot')
     (0, 9700, 34.6275672, 31.3217528, 'أوفاكيم', 'אופקים', 'Офаким', 'Ofakim')
     (0, 9800, 34.761651, 31.988176, 'ريشون لِتْسِيون - موشيه ديان', 'ראשון לציון - משה דיין', 'Ришон-Ле-Цион Моше Даян', 'Rishon LeTsiyyon - Moshe Dayan')

The second function prints the timetable for the selected station on a chosen day of the week and time.

    query_time_table('3100', chameshi, 9)

    Time  : P : Di : Train : Name
    ------:---:----:-------:-----------
    09:08 : 1 : NS :   407 : Beer Sheva Center
    09:10 : 2 : SN :   232 : Binyamina
    09:17 : 1 : NS :   235 : Rehovot E. Hadar
    09:18 : 2 : SN :   404 : Karmiel
    09:40 : 2 : SN :   234 : Binyamina
    09:47 : 1 : NS :   237 : Beer Sheva Center
    10:08 : 1 : NS :   409 : Beer Sheva Center
    10:10 : 2 : SN :   236 : Binyamina
    10:17 : 1 : NS :   239 : Rehovot E. Hadar
    10:18 : 2 : SN :   406 : Karmiel
    10:40 : 2 : SN :   238 : Binyamina

The third function prints all the stops for the selected train on the chosen day of the week:

    query_train_stops(227, chameshi)
    
     P :  Time  : Name
    ---:--------:---------------
     3 : 07:07  : Binyamina
     2 : 07:11  : Kesariyya - Pardes Hanna
     1 : 07:17  : Hadera West
     2 : 07:27  : Netanya
     1 : 07:32  : Netanya-Sapir
     1 : 07:35  : Bet Yehoshua
     4 : 07:43  : Herzliya
     2 : 07:49  : Tel Aviv - University
     4 : 07:56  : Tel Aviv Center
     2 : 07:58  : Tel Aviv HaShalom
     3 : 08:03  : Tel Aviv HaHagana
     2 : 08:14  : Lod - Ganey Aviv
     3 : 08:19  : Lod
     2 : 08:26  : Beer Yaakov
     2 : 08:32  : Rehovot E. Hadar

## What needs to be done

1. Add a Python script that extracts and saves the required data locally as JSON files;
2. Add a Python script that parses JSON files, prepares the data, and populates the database tables.
3. Bonus: Find a better, more optimal way to request and process the data. Currently, to avoid missing any stations or
   trains, I have to request all possible combinations of 'from' and 'to' stations for each day of the week through the
   API, which takes time.
4. Open-source the Android and iOS apps.

## Credits

For a long time, I had to reverse-engineer the [rail.co.il](https://rail.co.il) site and crawl the data to create the
database in a way that the app can work. Fortunately, recently, I found this repository with the unofficial API. It helped
me a lot and saved me a bunch of time, so kudos to @sh0oki!

[Unofficial Israel-Rail-API](https://github.com/sh0oki/israel-rail-api)

## Contributing

I'd love your contributions! Send a Pull request, and I'll be happy to approve it.

## Apple and Google App Stores

NextTrain is available on the Apple and Google App Stores. It's free and without ads.

[Apple Store](https://apps.apple.com/us/app/next-train-israel/id344549320)

[Google Play Store](https://play.google.com/store/apps/details?id=com.n2o.nexttrain)

## Contact

If you have any questions, suggestions, feedback, or offers, please feel free to reach out to me
by [email](mailto:sergeyn@answersolution.net) or find me
on [LinkedIn](https://www.linkedin.com/in/sergey-neskoromny-86662a10/)
