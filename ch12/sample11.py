# pip install folium
import folium

# 지도 실행
map = folium.Map(location = [37.566621, 126.978208], zoom_start = 12)
# 지도 보기
map.show_in_browser()