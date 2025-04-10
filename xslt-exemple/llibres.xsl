<!-- llibres.xsl -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head><title>Llistat de Llibres</title></head>
      <body>
        <h1>Llibres disponibles</h1>
        <table border = "1">
          <tr>
            <th>Títol</th>
            <th>Autor</th>
            <th>Pàgines</th>
          </tr>
          <xsl:for-each select="llibres/llibre">
            <tr>
              <td><xsl:value-of select="titol"/></td>
              <td><xsl:value-of select="autor"/></td>
              <td><xsl:value-of select="pagines"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
