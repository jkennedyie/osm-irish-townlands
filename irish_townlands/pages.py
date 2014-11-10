"""
Simple, non-DB, flatpage like feature
"""
PAGES = {
    'about': {
        'title': 'About Townlands.ie',
        'body': 'About',
    },

    'copyright': {
        'title': 'Copyright of Townlands.ie',

        'body': """
            <p>Since this is derived from <a href="openstreetmap.org">OpenStreeMap</a> data, it's under the same licence as that. Namely the <a href="http://opendatacommons.org/licenses/odbl/">Open Data Commons Open Database License (ODbL)</a>.</p>
            <p>Consult the <a href="http://www.openstreetmap.org/copyright">OpenStreetMap Copyright</a> guide for more informatiom.</p>
        """,
    },

    'download': {
        'title': 'Downloading Townlands.ie data',
        'body': """
            <p>The data from townlands.ie is available in many formats</p>
            <table class="table">
                <tr>
                    <th>Type of Data</th>
                    <th>Shapefile</th>
                    <th>GeoJSON</th>
                    <th>KML</th>
                </tr>
                <tr>
                    <td>Townlands</td>
                    <td><a href="/static/downloads/townlands.zip">download shapefile</a></td>
                    <td><a href="/static/downloads/townlands.geojson.gz">download GeoJSON</a></td>
                    <td><a href="/static/downloads/townlands.kmz">download KML</a></td>
                </tr>
                <tr>
                    <td>Civil Parishes</td>
                    <td><a href="/static/downloads/civil_parishes.zip">download shapefile</a></td>
                    <td><a href="/static/downloads/civil_parishes.geojson.zip">download GeoJSON</a></td>
                    <td><a href="/static/downloads/civil_parishes.kmz">download KML</a></td>
                </tr>
                <tr>
                    <td>Baronies</td>
                    <td><a href="/static/downloads/baronies.zip">download shapefile</a></td>
                    <td><a href="/static/downloads/baronies.geojson.zip">download GeoJSON</a></td>
                    <td><a href="/static/downloads/baronies.kmlz">download KML</a></td>
                </tr>
                <tr>
                    <td>Counties</td>
                    <td><a href="/static/downloads/counties.zip">download shapefile</a></td>
                    <td><a href="/static/downloads/counties.geojson.zip">download GeoJSON</a></td>
                    <td><a href="/static/downloads/counties.kmz">download KML</a></td>
                </tr>
            </table>

            <h2>Data format</h2>
            <p>The geometry is available in <a href="spatialreference.org/ref/epsg/wgs-84/">WSG 84 (aka EPSG 4326, aka "latitude and longitude")</a> projection system.</p>

            <p>There are 3 columns per entry:
                <dl class="dl-horizontal">
                    <dt>OSM_ID<dt>
                    <dd>Integer. The id of the object in the OSM database. If it's positive, it's a way; if it's negative, it's a relation. (Consult the <a href="http://wiki.openstreetmap.org/wiki/Elements">OSM data model</a> for more)</dd>
                    <dt>NAME<dt>
                    <dd>String. The name of the object. Should be the "common name". Almost certainly in English, but may be in Irish. <i>(NB: In the KML/KMZ file, this is NAME2 due to how ogr2ogr converts things. Suggestions welcome for how to fix this.)</i></dd>
                    <dt>NAME:GA<dt>
                    <dd>String. The name of the object in Irish.</dd>
                </dl>
            </p>

            <h2>Copyright & Licence</h2>
            <p>Since this is derived from <a href="openstreetmap.org">OpenStreeMap</a> data, it's under the same licence as that. Namely the <a href="http://opendatacommons.org/licenses/odbl/">Open Data Commons Open Database License (ODbL)</a>.</p>
            <p>Consult the <a href="http://www.openstreetmap.org/copyright">OpenStreetMap Copyright</a> guide for more informatiom.</p>

        """,
    },

    'data_freshness': {
        'title': "How up-to-date is Townlands.ie?",
        'body': """
            <p>Townlands.ie is updated every day. At the bottom of the page, you can see the date and time of the last import of data.</p>
            <p>We use the Ireland extracts from <a href="http://planet.openstreetmap.ie/">OSM Data for Ireland</a>.</p>
        """,
    },


}
