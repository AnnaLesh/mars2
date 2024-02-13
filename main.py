from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def i():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми '
                                                                                               'безжизненные пока '
                                                                                               'планеты.',
                      'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="https://w7.pngwing.com/pngs/16/806/png-transparent-planet-mars-illustration-earth-terrestrial-planet-mars-solar-system-mars-sphere-venus-astronomical-object-thumbnail.png" alt="альтернативный текст">
                        <p>Вот она какая, красная планета</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return """<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link href="static/css/style.css" rel="stylesheet" />
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                            
                          </head>
                          <body>
                            <h1 style="color:red">Жди нас, Марс!</h1>
                            <img src="static/img/mars.png" alt="альтернативный текст">
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-secondary">Человечество вырастает из детства</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-success">Человечеству мала одна планета</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-secondary">Мы сделаем обитаемыми безжизненные пока планеты</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-warning">И начнем с Марса!</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-danger">Присоединяйся!</a>
                          </body>
                        </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                      </head>
                      <body>
                      <h1 style="text-align:center; font-weight: bold">Анкета претендента</h1>
                      <h5 style="text-align:center">На участие в миссии</h5>
                        <form style="border: 1px solid black; margin-left:35%; width:30%; background-color:#FFCA86; padding: 10px 10px 10px 10px; margin-top: 20px">
                              <div class="mb-3">
                                <label for="exampleInputEmail1" class="form-label" ></label>
                                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите фамилию">
                              </div>
                              <div class="mb-3">
                                <label for="exampleInputEmail1" class="form-label" ></label>
                                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите имя">
                                <br>
                              </div>
                              <p>Какое у вас образование?</p>
                              <select class="form-select" aria-label="Пример выбора по умолчанию">
                                
                                  <option selected>Начальное</option>
                                  <option value="1">Среднее</option>
                                  <option value="2">Высшее</option>
                                  <option value="3">Я без образования, плак плак</option>
                                </select>
                              <p>Какие у вас есть профессии?</p>
                              <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Инженер-исследователь
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Инженер-строитель
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Пилот
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Метеоролог
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Инженер по жизнеобеспечению
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Врач
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Экобиолог
                                  </label>
                                </div>
                                <p>Укажите пол</p>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                  <label class="form-check-label" for="flexRadioDefault1">
                                    Мужской
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
                                  <label class="form-check-label" for="flexRadioDefault2">
                                    Женский
                                  </label>
                                </div>
                                <p>Почему вы хотите принять участие в миссии?</p>
                                <div class="input-group">
                                  <textarea class="form-control" aria-label="С текстовым полем"></textarea>
                                </div>
                                <p>Приложите фотографию</p>
                                <div class="input-group mb-3">
  <input type="file" class="form-control" id="inputGroupFile03" aria-describedby="inputGroupFileAddon03" aria-label="Выберите файл">
</div>
                              <div class="form-check">
                              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                              <label class="form-check-label" for="flexCheckDefault">
                                Готовы остаться на Марсе?
                              </label>
                              
                            </div>
                              
                              <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                                                  </body>
                                                </html>"""




@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</a>
                    <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item">составляет {rating}!</a>
                    <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-warning">Желаем удачи!</a>
                  </body>
                </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Карусель</title>
                  </head>
                  <body style="margin-top:30px; margin-left:30px">
                    <h1 style="color:purple; font-weight:bold">Котики спасут мир</h1>
                    <div id="carouselExample" class="carousel slide" style="width:500px">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="https://i.pinimg.com/564x/9e/bc/02/9ebc0219e877bcb545baa6ccbd5b11a8.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                          <img src="https://i.pinimg.com/564x/63/3a/60/633a608ad5641c76aa92c058794ae742.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                          <img src="https://i.pinimg.com/564x/18/32/1c/18321cf4bb11854f96bf4362ede4766b.jpg" class="d-block w-100" alt="...">
                        </div>
                      </div>
                      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Предыдущий</span>
                      </button>
                      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Следующий</span>
                      </button>
                    </div>
                  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
