#! /usr/bin/gawk -f

BEGIN {FS = "/"}

{genres[$2][++ngenres[$2]] = $1}

END {
  n = asorti(genres, artists);
  for (i = 1; i <= n; i++)
  {
    artist = artists[i]
    m = asort(genres[artist], genres_of_artist)

    if (m > 1)
    {
      print "   " artist

      for (j = 1; j <= m; j++)
      {
        print "      " genres_of_artist[j]
      }
    }
  }
}
