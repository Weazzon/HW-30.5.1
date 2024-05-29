from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC




def test_show_my_pets(selenium_driver):
    '''Этот тест проверяет, что на сайте присутствуют все питомцы пользователя'''
    driver = selenium_driver
     # Проверяем, что мы оказались на главной странице пользователя
    #Явные ожидания
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH,'//*[@id="navbarNav"]/ul/li[1]/a').click()



    #Находим количество питомцев, отображенную на сайте
    WDW(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]

    #Находим таблицу со всеми моими питомцами
    # Неявные ожидания
    driver.implicitly_wait(2)
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert  int(pets_number) == len(pets_count),f'Указанное число моих питомцев - {int(pets_number)} не равно количеству присутствующих питомцев в таблице {len(pets_count)} '

def test_photo_pets(selenium_driver):
    '''Тест проверяет, что у более половины питомцев есть фотографии'''
    driver = selenium_driver
    # Проверяем, что мы оказались на главной странице пользователя
    # Явные ожидания
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()


    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    #Находим питомцев у которых есть фото

    # Неявные ожидания
    driver.implicitly_wait(2)
    image_count = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/")]')


    assert len(image_count) > ((len(pets_count) % 2) == 0),f'Количество питомцев с фото {len(image_count)} составляет меньше половины всех моих питомцев {len(pets_count)}'




def test_allpet_have_name_breed_age(selenium_driver):
    '''Тест проверяет, что все питомцы содержат данные
    имя, возраст, породу, и нет двух питомцев с одинаковыми именами
    '''
    driver = selenium_driver
    # Проверяем, что мы оказались на главной странице пользователя
    # Явные ожидания
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    #Находим таблицу со всеми питомцами
    # Неявные ожидания
    driver.implicitly_wait(2)
    allpet_count = driver.find_elements(By.XPATH,
        '//*[@id="all_my_pets"]/table/tbody/tr/td[1] | //*[@id="all_my_pets"]/table/tbody/tr/td[2] | //*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    names=set()

    for i in range(1, len(allpet_count) // 3 + 1):
        driver.implicitly_wait(2)
        name = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]').text
        driver.implicitly_wait(2)
        breed = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[2]').text
        driver.implicitly_wait(2)
        age = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[3]').text

        assert name and breed and age,f'Питомец {i}: Имеет Имя: {name}, Порода: {breed}, Возраст: {age}'

        assert name not in names, f'Имя животного {name} встречается больше одного раза'
        names.add(name)

def test_not_pet_same_name_breed_age(selenium_driver):
    '''Этот тест проверяет, что  нет двух питомцев с одинаковым именем, возрастом и породой
    '''
    driver = selenium_driver
    # Проверяем, что мы оказались на главной странице пользователя
    # Явные ожидания
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    #Находим таблицу со всеми питомцами
    # Неявные ожидания
    driver.implicitly_wait(2)
    allpet_count = driver.find_elements(By.XPATH,
        '//*[@id="all_my_pets"]/table/tbody/tr/td[1] | //*[@id="all_my_pets"]/table/tbody/tr/td[2] | //*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    pet_info=set()

    for i in range(1, len(allpet_count) // 3 + 1):
        driver.implicitly_wait(2)
        name = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]').text
        driver.implicitly_wait(2)
        breed = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[2]').text
        driver.implicitly_wait(2)
        age = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[3]').text

        pet_data = (name, age, breed)
        assert pet_data not in pet_info, f'Питомец {name} имеет двойник:)))'

        print(f'Питомец {i}: Имеет Имя: {name}, Порода: {breed}, Возраст: {age}')

        pet_info.add(pet_data)

