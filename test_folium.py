import folium
import os
import json

latFulda = 50.5558
lngFulda = 9.6808
# Create map object
m = folium.Map(location=[latFulda, lngFulda], zoom_start=10)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

# Vega data
vis = os.path.join('data', 'vis.json')

# Geojson Data
overlay = os.path.join('data', 'overlay.json')

# Create markers
folium.Marker([latFulda, lngFulda],
              popup='<strong>Fulda</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([latFulda + 0.05, lngFulda],
              popup='<strong>Cloudy</strong>',
              tooltip=tooltip,
              icon=folium.Icon()).add_to(m),
folium.Marker([latFulda - 0.05, lngFulda],
              popup='<strong>Purple Pin</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([latFulda, lngFulda + 0.05],
              popup='<strong>Green Leaf</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([latFulda, lngFulda - 0.05],
              popup='<strong>Location Five</strong>',
              tooltip=tooltip,
              icon=logoIcon).add_to(m),
folium.Marker([latFulda, lngFulda + 0.1],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)

# Circle marker
folium.CircleMarker(
    location=[latFulda, lngFulda + 0.2],
    radius=50,
    popup='My Birthplace',
    color='red',
    fill=True,
    fill_color='pink'
).add_to(m)

# Geojson overlay
folium.GeoJson(overlay, name='fulda').add_to(m)

# Generate map
m.save('Fulda.html')
