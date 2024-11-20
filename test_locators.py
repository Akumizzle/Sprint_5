reg_name='.//fieldset[1]//input' #поле имя на странице регистрации
reg_pass='.//fieldset[3]//input' #поле пароль на странице регистрации
reg_email='.//fieldset[2]//input' #поле email на странице регистрации
reg_button='.button_button__33qZ0' #кнопка "зарегистрироваться" на странице регистрации
reg_warning=".//p[text()='Некорректный пароль']" #надпись "некорректный пароль" на странице регистрации

login_email=".//input[@type='text']" #поле email на странице входа
login_pass=".//input[@type='password']" #поле пароль на странице входа
login_button='.button_button__33qZ0' #кнопка "войти"

button_enter=".//button[text()='Войти']"
button_signin=".//button[text()='Войти в аккаунт']" #кнопка "войти в аккаунт"
button_order=".//button[text()='Оформить заказ']" #кнопка "оформить заказ"
button_logout='.Account_button__14Yp3' #кнопка "выход"
constructor='.BurgerIngredients_ingredients__menuContainer__Xu3Mo' #конструктор

text_vhod=".//h2[text()='Вход']"

text_sauce=".//h2[text()='Соусы']"
text_filling=".//h2[text()='Начинки']"
text_bread=".//h2[text()='Булки']"
button_sause=".//span[text()='Соусы']"
button_filling=".//span[text()='Начинки']"
button_bread=".//span[text()='Булки']"
buttons=['.AppHeader_header__list__3oKJj > li:nth-child(1)','.AppHeader_header__logo__2D0X2 > a:nth-child(1)']