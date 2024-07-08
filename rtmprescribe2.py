import time
import security3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URLLogin = 'https://dev.everex.ai/signin'
account3 = security3.account2()

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url=URLLogin)

wait = WebDriverWait(driver, 10)  # 최대 10초 대

#쿠키창 노출 > 쿠키 허가 (쿠키는 모두 허가함)
cookieconsent = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div')
managecookieBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/button')

if managecookieBtn:
 print("managecookieBtn")

managecookieBtn.click()

cookieacptBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/button[2]')
if cookieacptBtn:
 print("cookieacptBtn")

cookierejtBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/button[1]')
if cookierejtBtn:
 print("cookierejtBtn")

time.sleep(1)

 
# 쿠키 설정 변경 (쿠키는 모두 허가함)
AnalyticalCookiesBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[2]/div[2]/label/span')
AnalyticalCookiesBtn.click()
time.sleep(1)

PerformanceCookiesBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[3]/div[2]/label/span')
PerformanceCookiesBtn.click()
time.sleep(1)

SaveMyPreferencesBtn = cookieconsent.find_element(By.XPATH, "//*[text()='Save My Preferences']")
SaveMyPreferencesBtn.click()
time.sleep(1)


# 로그인
emailinput = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div')
emailinput.click()
input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/input').send_keys(account3.get("email"))
time.sleep(3)
input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/input').send_keys(account3.get("password"))
time.sleep(3)
loginBtn = driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div[2]/div/button')
loginBtn.click()

print("쿠키 모두 허가 후 로그인 성공")

wait = WebDriverWait(driver, 10)

# patientlist 요소 로드
patientlist = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div')))
time.sleep(3)

# 동일한 클래스를 가진 요소들 찾기
elements = driver.find_elements(By.CSS_SELECTOR, "._patient_list__area_1eqzq_24")

# n번째 요소를 클릭 (n은 0부터 시작하는 인덱스)
n = 4  # 예를 들어 네 번째 요소를 클릭하려면 3을 사용
if len(elements) > n:
    elements[n].click()
    print(f"{n + 1}번째 요소를 클릭했습니다!")
else:
    print(f"요소의 수가 충분하지 않습니다. 총 요소 수: {len(elements)}")

time.sleep(5)

# 운동 처방 버튼 클릭
PrescribeBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/button')
PrescribeBtn.click()
time.sleep(2)  # 충분한 대기 시간을 확보

# 운동 배정해보기
ExerciseBtn = driver.find_element(By.XPATH, ".//div[p[text()='Exercises']]")
ExerciseBtn .click()
time.sleep(2)
    
addBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/button[2]')
addBtn.click()
time.sleep(2)
    
selectallBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div/div[2]/button[1]/span')
selectallBtn.click()
time.sleep(2)
    
SetdateBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[3]/button')
SetdateBtn.click()
time.sleep(2)

# 캘린더에서 무작위로 1개의 버튼 클릭
# 페이지 로딩 대기
wait = WebDriverWait(driver, 10)

try:
    # 'calender1' 요소가 로드될 때까지 대기
    found = False
    calender1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]')))
    weekBox = calender1.find_elements(By.CLASS_NAME, "_dualaWeekBox_d7c92_173")
    for week in weekBox:
        dateDiv = week.find_elements(By.CSS_SELECTOR, "div")
        for day in dateDiv:
            className = day.get_attribute('class')
            if "pass" not in className and "hidden" not in className:
                found = True
                day.click()
                break
        if found:
            break
    if not found:
        print("캘린더1 내에서 클릭할 수 있는 날짜가 없습니다.")
    else:
        print("캘린더1에서 날짜를 클릭했습니다.")
except Exception as e:
    print(f"캘린더1 내에서 버튼을 클릭하는 도중 오류가 발생했습니다: {e}")

time.sleep(2)

# 두번째 달력에서 날짜 선택하기 (날짜는 15로)
try:
    found = False
    calender2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]')))
    weekBox = calender2.find_elements(By.CLASS_NAME, "_dualaWeekBox_d7c92_173")
    
    
    for week in weekBox:
        dateDiv = week.find_elements(By.CSS_SELECTOR, "div")
        for day in dateDiv:
            className = day.get_attribute('class')
            dayText = day.text
            if "pass" not in className and "hidden" not in className and dayText == "15":
                found = True
                day.click()
                n -= 1
                if n == 0:
                    break  # 원하는 순서에 도달하면 종료
        if found:
            break
    if not found:
        print("캘린더2 내에서 클릭할 수 있는 날짜가 없습니다.")
    else:
        print("캘린더2에서 두 번째 날짜를 클릭했습니다.")
except Exception as e:
    print(f"캘린더2 내에서 버튼을 클릭하는 도중 오류가 발생했습니다: {e}")

time.sleep(2)


continuebtn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div/button[2]')))
continuebtn.click()
print('클릭')
time.sleep(2)

continuebtn2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[3]/button')
continuebtn2.click()
time.sleep(2)

# ExerciseRegion 요소를 대기하여 찾습니다.
ExerciseRegion = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_exercise_region_body_ynwom_40")))

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Shoulder'인 div 요소를 찾습니다.
Shoulder_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Shoulder']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Elbow'인 div 요소를 찾습니다.
Elbow_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Elbow']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Wrist & Hand'인 div 요소를 찾습니다.
Wrist_Hand_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Wrist & Hand']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Hip & Pelvic'인 div 요소를 찾습니다.
Hip_Pelvic_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Hip & Pelvic']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Knee'인 div 요소를 찾습니다.
Knee_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Knee']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Ankle & Foot'인 div 요소를 찾습니다.
Ankle_Foot_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Ankle & Foot']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Cervical'인 div 요소를 찾습니다.
Cervical_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Cervical']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Thoracic'인 div 요소를 찾습니다.
Thoracic_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Thoracic']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Lumbar'인 div 요소를 찾습니다.
Lumbar_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Lumbar']]")

# ExerciseRegion 내부에서 p 태그의 텍스트가 'Abdomen'인 div 요소를 찾습니다.
Abdomen_div = ExerciseRegion.find_element(By.XPATH, ".//div[p[text()='Abdomen']]")

# 해당 요소를 클릭합니다.
Lumbar_div.click()

plan_name_wrapper = wait.until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'plan_name_body')]")))
plan_name_wrapper.click()
time.sleep(2)
input_focus = wait.until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'input_focus')]")))

 # 요소가 존재하는지 확인
if input_focus:
 print("Found input_focus")
    
# JavaScript로 텍스트 설정
driver.execute_script("arguments[0].innerText = 'everex';", input_focus)
time.sleep(2)

Precaution = driver.find_element(By.CLASS_NAME, "_precaution_body_1mlcl_30")

# 1번 요구 사항 체크하기
PrecautionBtn1 = Precaution.find_element(By.XPATH, "//*[text()='Please apply ice after exercising']")
checkbox_input1 = PrecautionBtn1.find_element(By.XPATH, "..//input[@type='checkbox']")
if PrecautionBtn1:
 print("PrecautionBtn1")

# 2번 요구 사항 체크하기
PrecautionBtn2 = Precaution.find_element(By.XPATH, "//*[text()='If you experience severe pain, please discontinue exercising']")
checkbox_input2 = PrecautionBtn2.find_element(By.XPATH, "..//input[@type='checkbox']")
if PrecautionBtn2:
 print("PrecautionBtn2")

# 3번 요구 사항 체크하기
PrecautionBtn3 = Precaution.find_element(By.XPATH, "//*[text()='Please stretch both before and after exercising']")
checkbox_input3 = PrecautionBtn3.find_element(By.XPATH, "..//input[@type='checkbox']")
if PrecautionBtn3:
 print("PrecautionBtn3")

# 4번 요구 사항 체크하기
PrecautionBtn4 = Precaution.find_element(By.XPATH, "//*[text()='Please write a personalized precaution within 150 characters']")
checkbox_input4 = PrecautionBtn4.find_element(By.XPATH, "..//input[@type='checkbox']")
if PrecautionBtn4:
 print("PrecautionBtn4")

checkbox_input1.click()
checkbox_input2.click()
checkbox_input3.click()
checkbox_input4.click()
time.sleep(1)

AIFunctionalMeasure = driver.find_elements(By.CLASS_NAME, '_ft_wrapper_wz06z_6')

Upperhalf = driver.find_element(By.XPATH, "//*[text()='Upper half']")
Upperhalf.click()
time.sleep(1)

# Upperhalf 부위 선택 준비

sidelateralraiseright = Upperhalf.find_element(By.XPATH, "//*[text()='Side Lateral Raise (Right)']")
sideinput1 = sidelateralraiseright.find_element(By.XPATH, "..//input[@type='checkbox']")

sidelateralraiseleft = Upperhalf.find_element(By.XPATH, "//*[text()='Side Lateral Raise (Left)']")
sideinput2 = sidelateralraiseleft.find_element(By.XPATH, "..//input[@type='checkbox']")

frontarmraiseright = Upperhalf.find_element(By.XPATH, "//*[text()='Front Arm Raise (Right)']")
frontinput1 = frontarmraiseright.find_element(By.XPATH, "..//input[@type='checkbox']")

frontarmraiseleft = Upperhalf.find_element(By.XPATH, "//*[text()='Front Arm Raise (Left)']")
frontinput2 = frontarmraiseleft.find_element(By.XPATH, "..//input[@type='checkbox']")

elblowflexionright = Upperhalf.find_element(By.XPATH, "//*[text()='Elbow Flexion (Right)']")
elbowinput1 = elblowflexionright.find_element(By.XPATH, "..//input[@type='checkbox']")

elblowflexionleft = Upperhalf.find_element(By.XPATH, "//*[text()='Elbow Flexion (Left)']")
elbowinput2 = elblowflexionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

elblowextensionright = Upperhalf.find_element(By.XPATH, "//*[text()='Elbow Extension (Right)']")
elbowexinput1 = elblowextensionright.find_element(By.XPATH, "..//input[@type='checkbox']")

elblowextensionleft = Upperhalf.find_element(By.XPATH, "//*[text()='Elbow Extension (Left)']")
elbowexinput2 = elblowextensionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

sideinput1.click()
sideinput2.click()
frontinput1.click()
frontinput2.click()
elbowinput1.click()
elbowinput2.click()
elbowexinput1.click()
elbowexinput2.click()
time.sleep(1)

#Lowerhalf 부위 선택 준비
Lowerhalf = driver.find_element(By.XPATH, "//*[text()='Lower half']")
Lowerhalf.click()
time.sleep(1)

hipflexionright = Lowerhalf.find_element(By.XPATH, "//*[text()='Hip Flexion (Right)']")
hipinput1 = hipflexionright.find_element(By.XPATH, "..//input[@type='checkbox']")

hipflexionleft = Lowerhalf.find_element(By.XPATH, "//*[text()='Hip Flexion (Left)']")
hipinput2 = hipflexionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

hipextensionright = Lowerhalf.find_element(By.XPATH, "//*[text()='Hip Extension (Right)']")
hipexinput1 = hipextensionright.find_element(By.XPATH, "..//input[@type='checkbox']")

hipextensionleft = Lowerhalf.find_element(By.XPATH, "//*[text()='Hip Extension (Left)']")
hipexinput2 = hipextensionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

hipabductionright = Lowerhalf.find_element(By.XPATH, "//*[text()='Hip Abduction (Right)']")
hipabinput1 = hipabductionright.find_element(By.XPATH, "..//input[@type='checkbox']")

hipabductionleft = Lowerhalf.find_element(By.XPATH, "//*[text()='Hip Abduction (Left)']")
hipabinput2 = hipabductionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

kneeflexionright = Lowerhalf.find_element(By.XPATH, "//*[text()='Knee Flexion (Right)']")
kneeinput1 = kneeflexionright.find_element(By.XPATH, "..//input[@type='checkbox']")

kneeflexionleft = Lowerhalf.find_element(By.XPATH, "//*[text()='Knee Flexion (Left)']")
kneeinput2 = kneeflexionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

kneeextensionright = Lowerhalf.find_element(By.XPATH, "//*[text()='Knee Extension (Right)']")
kneeexinput1 = kneeextensionright.find_element(By.XPATH, "..//input[@type='checkbox']")

kneeextensionleft = Lowerhalf.find_element(By.XPATH, "//*[text()='Knee Extension (Left)']")
kneeexinput2 = kneeextensionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

hipinput1.click()
hipinput2.click()
hipexinput1.click()
hipexinput2.click()
hipabinput1.click()
hipabinput2.click()
kneeinput1.click()
kneeinput2.click()
kneeexinput1.click()
kneeexinput2.click()
time.sleep(3)

#Trunk 부위 선택 준비
Trunk = driver.find_element(By.XPATH, "//*[text()='Trunk']")
Trunk.click()
time.sleep(1)

trunkflexionforward = Trunk.find_element(By.XPATH, "//*[text()='Trunk Flexion (Forward)']")
trunkinput1 = trunkflexionforward.find_element(By.XPATH, "..//input[@type='checkbox']")

trunkextensionbackward = Trunk.find_element(By.XPATH, "//*[text()='Trunk Extension (Backward)']")
trunkinput2 = trunkextensionbackward.find_element(By.XPATH, "..//input[@type='checkbox']")

lateraltrunkflexionright = Trunk.find_element(By.XPATH, "//*[text()='Lateral Trunk Flexion (Right)']")
ltfexinput1 = lateraltrunkflexionright.find_element(By.XPATH, "..//input[@type='checkbox']")

lateraltrunkflexionleft = Trunk.find_element(By.XPATH, "//*[text()='Lateral Trunk Flexion (Left)']")
ltfexinput2 = lateraltrunkflexionleft.find_element(By.XPATH, "..//input[@type='checkbox']")

trunkinput1.click()
trunkinput2.click()
ltfexinput1.click()
ltfexinput2.click()
time.sleep(1)

continuebtn3 = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[3]/button[2]')
continuebtn3.click()
time.sleep(2)

decisionBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[3]/button[2]')
decisionBtn.click()
time.sleep(2)

# 반복 등록이 완료되면 브라우저 종료
time.sleep(100)
