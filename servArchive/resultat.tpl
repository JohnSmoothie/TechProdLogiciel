<!DOCTYPE>
<html>
<meta charset="utf-8">
<head>
</head>
<body>
  <table>
    <tr>
      <td>Activites</td>
      <td>Ville</td>
      <td>Installations</td>
    </tr>
    <tr>
      %for row in rows :
        <td>{{row}}</td>
      %end
    </tr>
    <tr>

    </tr>

  </table>
  <ul>
    %for row in rows :
      <li>{{row}}</li>
    %end
  </ul>
</body>
</HTML>
