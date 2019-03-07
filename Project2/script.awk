#! /usr/bin/gawk -f

BEGIN {FS = "/"}

{
  # input only distinct albums
  if ($4 != prev_album)
  {
    albums[$3][++nalbums[$3]] = $4
    prev_album = $4
  }

  # since there are two types of track path
  if (NF == 5)
  {
    # array for tracks
    tracks[$3][$4][++ntracks[$4]] = $5

    # array for track paths
    trackPaths[$3][$4][++ntrackPaths[$4]] = $0
  }
  else if (NF == 6)
  {
    tracks[$3][$4][++ntracks[$4]] = $6

    trackPaths[$3][$4][++ntrackPaths[$4]] = $0
  }
}

END {
  print "<html>"
  print " <meta http-equiv=\42content-type\42 content=\42text/html; charset=utf-8\42 />"
  print "<body>"
  print "<table border=\42 1 \42>"
  print "  <tr>"
  print "    <th>Artist</th>"
  print "    <th>Album</th>"
  print "    <th>Tracks</th>"
  print "  </tr>"

  n = asorti(albums, artists)

  for (i = 1; i <= n; i++)
  {
    artist = artists[i]

    nn = asort(albums[artist], albums_of_artist)

    print "  <tr>"
    print "    <td rowspan=\42" nn "\42>" artist "</td>"

    for (ii = 1; ii <= nn; ii++)
    {
      album = albums_of_artist[ii]

      if (ii != 1)
      {
        print "  <tr>"
      }
      print "    <td>" album "</td>"
      print "    <td>"
      print "      <table border=\42 0 \42>"

      m = asort(tracks[artist][album], tracks_of_album)
      mm = asort(trackPaths[artist][album], trackPaths_of_album)

      for (j = 1; j <= m; j++)
      {
        track = tracks_of_album[j]
        trackPath = trackPaths_of_album[j]
        print "        <tr><td><a href=\42" trackPath "\42>" track "</a></td></tr>"
      }

      print "      </table>"
      print "    </td>"
      print "  </tr>"
      }
  }
  print "</table>"
  print "</body>"
  print "</html>"
}
