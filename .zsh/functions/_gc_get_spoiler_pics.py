#compdef gc_get_spoiler_pics.py gc_get_spoiler_pics ~/gc_get_spoiler_pics.py

_arguments '--lat_offset[Latitude Offset for Images Geotag]' \
   '--lon_offset[Longitude Offset for Images Geotag]' \
   '--savedir[Directory to save images in]:savedir:_files -/' \
   '--filter[Regex that needs to match the Image Description]' \
   '--threads[use <num> threads, 0 disables threading, default is number of CPUs]:number of threads:({0..100})' \
   '( -s --skip_present )'{-s,--skip_present}'[skip GC with pictures present in savedir]' \
   '( -d --done_file )'{-d,--done_file}'[use and update list of already processed GC]' \
   '( -g --no_geotag )'{-g,--no_geotag}"[don't geotag images]" \
   '( -x --delete_old )'{-x,--delete_old}'[delete images of gc not found in given gpx]' \
   '( -f --flat )'{-f,--flat}'[All in one directory, no GeocachePhotos subdirs]' \
   '( -h --help )'{-h,--help}'[Show Help]' \
   '*:Pocket Queries:_files -g "*.(#i)gpx"'
