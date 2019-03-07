#! /usr/bin/gawk -f

BEGIN {FS = "/"}

{albums[$1][++nalbums[$1]] = $2}

END {
  n = asorti(albums, artists);
  for (i = 1; i <= n; i++)
  {
    artist = artists[i]
    m = asort(albums[artist], albums_of_artist)

    print "   " artist

    for (j = 1; j <= m; j++)
    {
      print "      " albums_of_artist[j]
    }
  }
}
