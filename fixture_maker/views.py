from django.http import HttpResponse
from django.shortcuts import render
from tabulate import tabulate
import random
import math

l = []
numteam = [0]
vs = []
vs.clear()
for i in range(32):
    vs.append('VS')

def index(request):
    return render(request, 'index.html')

def inputPage(request):
    numteam.clear()
    numteam.append(request.GET.get('selectTeams'))

    team1 = request.GET.get('team1', 'Bye')
    team2 = request.GET.get('team2', 'Bye')
    team3 = request.GET.get('team3', 'Bye')
    team4 = request.GET.get('team4', 'Bye')
    team5 = request.GET.get('team5', 'Bye')
    team6 = request.GET.get('team6', 'Bye')
    team7 = request.GET.get('team7', 'Bye')
    team8 = request.GET.get('team8', 'Bye')
    team9 = request.GET.get('team9', 'Bye')
    team10 = request.GET.get('team10', 'Bye')
    team11 = request.GET.get('team11', 'Bye')
    team12 = request.GET.get('team12', 'Bye')
    team13 = request.GET.get('team13', 'Bye')
    team14 = request.GET.get('team14', 'Bye')
    team15 = request.GET.get('team15', 'Bye')
    team16 = request.GET.get('team16', 'Bye')
    team17 = request.GET.get('team17', 'Bye')
    team18 = request.GET.get('team18', 'Bye')
    team19 = request.GET.get('team19', 'Bye')
    team20 = request.GET.get('team20', 'Bye')
    team21 = request.GET.get('team21', 'Bye')
    team22 = request.GET.get('team22', 'Bye')
    team23 = request.GET.get('team23', 'Bye')
    team24 = request.GET.get('team24', 'Bye')
    team25 = request.GET.get('team25', 'Bye')
    team26 = request.GET.get('team26', 'Bye')
    team27 = request.GET.get('team27', 'Bye')
    team28 = request.GET.get('team28', 'Bye')
    team29 = request.GET.get('team29', 'Bye')
    team30 = request.GET.get('team30', 'Bye')
    team31 = request.GET.get('team31', 'Bye')
    team32 = request.GET.get('team32', 'Bye')
    
    l.clear()
    
    l.append(team1.upper())
    l.append(team2.upper())
    l.append(team3.upper())
    l.append(team4.upper())
    l.append(team5.upper())
    l.append(team6.upper())
    l.append(team7.upper())
    l.append(team8.upper())
    l.append(team9.upper())
    l.append(team10.upper())
    l.append(team11.upper())
    l.append(team12.upper())
    l.append(team13.upper())
    l.append(team14.upper())
    l.append(team15.upper())
    l.append(team16.upper())
    l.append(team17.upper())
    l.append(team18.upper())
    l.append(team19.upper())
    l.append(team20.upper())
    l.append(team21.upper())
    l.append(team22.upper())
    l.append(team23.upper())
    l.append(team24.upper())
    l.append(team25.upper())
    l.append(team26.upper())
    l.append(team27.upper())
    l.append(team28.upper())
    l.append(team29.upper())
    l.append(team30.upper())
    l.append(team31.upper())
    l.append(team32.upper())
    
    # changing the null strings to bye
    for i in range(len(l)):
        if l[i] == '':
            l[i] = 'BYE'

    #for knockout rounds

    #to find the nnearest number which is a power of 2

    if int(numteam[0]) % 2 != 0:
        next = int(math.pow(2, math.ceil(math.log(int(numteam[0]))/math.log(2))))
    
        #dividing and arranging the teams

        end1ind = int(next/2)
        end2ind = int(next)
    else:
        end1ind = int(int(numteam[0])/2)
        end2ind = int(int(numteam[0]))
    
    #error
    x = l[0:end1ind]
    y = l[end1ind:end2ind]
    random.shuffle(x)
    random.shuffle(y)
    z = list(zip(x,vs,y))
    table = (tabulate(z,tablefmt='html', headers=['TEAM 1', 'VS', 'TEAM 2']))

    f = open('templates\knockout.html', 'w')
    html = f'''  <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>KNOCKOUT</title>
                    <!--bootstrap-->
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
                        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

                    <!--add js stattic file-->''' + '''<style>
                        table {
                            border-collapse: collapse;
                            margin: 25px 0;
                            font-size: 0.9em;
                            min-width: 400px;
                            border-radius: 5px 5px 0 0;
                            overflow: hidden;
                            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                            width: 100%;
                            margin-top: 2%;
                            margin-bottom: 5%;
                        }

                        table thead tr {
                            background-color: #009879;
                            color: #ffffff;
                            font-size: large;
                            text-align: center;
                            font-weight: bold;
                        }

                        table th,
                        table td {
                            padding: 12px 15px;
                        }

                        table tbody tr {
                            border-bottom: 1px solid #dddddd;
                        }

                        table tbody tr:nth-of-type(even) {
                            background-color: #f3f3f3;
                        }

                        table tbody tr:last-of-type {
                            border-bottom: 2px solid #009879;
                        }

                        table tbody tr.active-row {
                            font-weight: bold;
                            color: #009879;
                        }
                    </style>
                </head>''' + f'''<body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
                        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
                        crossorigin="anonymous"></script>
                    <div style="width : 100%; height: 100%; position: fixed; left: 14%; display : block; text-align: center;">
                        <!-- As a heading -->
                        <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark" style="height: 7%;">
                            <div class="container-fluid" style=" text-align: center;">
                                <text
                                    style="color: white; margin-left: 40.4%; font-size: x-large; font-family:Verdana, Geneva, Tahoma, sans-serif"></text>
                            </div>
                        </nav>
                        <div style="overflow-y: auto; height: 100%; width : 100%">
                        <div class="mb-3" style="margin-top: 5%; text-align: center; height: 100%; width: 60%; margin-left: 14%; margin-right: 21%; margin-top: 2%; align-items: center;">
                            <!--<label style="color: black; font-size: x-large; font-family:Verdana, Geneva, Tahoma, sans-serif">ROUND 1</label>-->

                            {table}
                        </div>
                        </div>
                    </div>

                    <div class="d-flex flex-column flex-shrink-0 p-3 text-bg-dark"
                        style="width: 15%; height: 100%; position: fixed; left: 0; top : 0; display: block;">
                        <div style="height: fit-content; text-align: center;">
                            <text
                                style="align-self: center; font-size: x-large; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif ;">
                                MAKE YOUR FIXTURES </text>
                        </div>
                        <hr>
                        <ul class="nav nav-pills flex-column mb-auto">
                            <li class="nav-item">
                                <a href="/" class="nav-link text-white" aria-current="page">
                                    Home
                                </a>
                            </li>
                            <li>
                                <a href="/roundrobin" class="nav-link text-white">
                                    League
                                </a>
                            </li>
                            <li>
                                <a href="/knockout" class="nav-link active">
                                    Knockout
                                </a>
                            </li>
                        </ul>
                        <hr>
                        <div class="dropdown" style="text-align: center;">
                            <text style="align-self: center; font-family: 'Courier New', Courier, monospace; font-size: x-large">FIXTURE
                                MAKER</text>
                        </div>
                    </div>
                </body>

                </html>'''
    
    f.write(html)
    f.close()

    #for roundrobin rounds
    if int(numteam[0])%2 != 0:
        r1end = int((int(numteam[0]) + 1)/2)
        r2end = int(int(numteam[0])+1)
        a = l[0: r1end]
        b = l[r1end:r2end]
    else:
        r1end = int(int(numteam[0])/2)
        r2end = int(int(numteam[0]))
        a = l[0: r1end]
        b = l[r1end:r2end]

    roundrobin = f'''  <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>LEAGUE</title>
                    <!--bootstrap-->
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
                        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

                    <!--add js stattic file-->''' + '''<style>
                        table {
                            border-collapse: collapse;
                            margin: 25px 0;
                            font-size: 0.9em;
                            min-width: 400px;
                            border-radius: 5px 5px 0 0;
                            overflow: hidden;
                            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                            width: 100%;
                            margin-top: 2%;
                            margin-bottom : 5%;
                        }

                        table thead tr {
                            background-color: #009879;
                            color: #ffffff;
                            font-size: large;
                            text-align: center;
                            font-weight: bold;
                        }

                        table th,
                        table td {
                            padding: 12px 15px;
                        }

                        table tbody tr {
                            border-bottom: 1px solid #dddddd;
                        }

                        table tbody tr:nth-of-type(even) {
                            background-color: #f3f3f3;
                        }

                        table tbody tr:last-of-type {
                            border-bottom: 2px solid #009879;
                        }

                        table tbody tr.active-row {
                            font-weight: bold;
                            color: #009879;
                        }
                    </style>
                </head>''' + f'''<body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
                        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
                        crossorigin="anonymous"></script>
                    <div style="width : 100%; height: 100%; position: fixed; left: 14%; display : block; text-align: center;">
                        <!-- As a heading -->
                        <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark" style="height: 7%;">
                            <div class="container-fluid" style=" text-align: center;">
                                <text
                                    style="color: white; margin-left: 40.4%; font-size: x-large; font-family:Verdana, Geneva, Tahoma, sans-serif"></text>
                            </div>
                        </nav>
                        <div style="overflow-y: auto; height: 100%; width : 100%">
                        <div class="mb-3" style="margin-top: 5%; text-align: center; height: 100%; width: 60%; margin-left: 14%; margin-right: 21%; margin-top: 2%; align-items: center;">
                            '''

    # rotation of first list
    count = 1
    for i in range(len(a)):
        m = a.pop()
        a.insert(0, m)
        n = list(zip(a,vs,b))
        rt = (tabulate(n,tablefmt='html', headers=['TEAM 1', 'VS', 'TEAM 2']))
        roundrobin = roundrobin + f'''<label style="color: black; font-size: x-large; font-family:Verdana, Geneva, Tahoma, sans-serif">ROUND {count}</label> {rt} <br>'''
        count += 1
    
    roundrobin = roundrobin + '''</div>
                    </div>
                    </div>

                    <div class="d-flex flex-column flex-shrink-0 p-3 text-bg-dark"
                        style="width: 15%; height: 100%; position: fixed; left: 0; top : 0; display: block;">
                        <div style="height: fit-content; text-align: center;">
                            <text
                                style="align-self: center; font-size: x-large; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif ;">
                                MAKE YOUR FIXTURES </text>
                        </div>
                        <hr>
                        <ul class="nav nav-pills flex-column mb-auto">
                            <li class="nav-item">
                                <a href="/" class="nav-link text-white" aria-current="page">
                                    Home
                                </a>
                            </li>
                            <li>
                                <a href="/roundrobin" class="nav-link text active">
                                    League
                                </a>
                            </li>
                            <li>
                                <a href="/knockout" class="nav-link text-white">
                                    Knockout
                                </a>
                        </ul>
                        <hr>
                        <div class="dropdown" style="text-align: center;">
                            <text style="align-self: center; font-family: 'Courier New', Courier, monospace; font-size: x-large">FIXTURE
                                MAKER</text>
                        </div>
                    </div>
                </body>

                </html>'''
    
    f = open('templates/roundrobin.html', 'w')

    f.write(roundrobin)
    f.close()

        

    return render(request, 'index.html')

def roundrobin(request):

    return render(request, 'roundrobin.html')

def knockout(request):
    
    return render(request, 'knockout.html')
