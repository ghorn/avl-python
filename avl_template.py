
template = """
! Name
Partridge
! Mach number
0.05
! IYsym      IZsym      Zsym
0            0          0
! Sref       Cref       Bref
0.596        0.1875   	1.5
! Xref       Yref       Zref
-0.35         0.0       0.0

!!!!!!!!!!!!!!!!!!!!!!!! Front Wing
SURFACE
1 (Front Wing)
!Nchordwise  Cspace    Nspanwise   Sspace
10   1.0   40   1.0
YDUPLICATE
0.0
TRANSLATE
%(fw_trans)s
!----------------------------------
! Section 0
SECTION
!Xle    Yle    Zle    Chord    Ainc
0    0    0   0.1875    0.0
!mh114.dat at Re = 200000
CLAF
1.0
CDCL
0.3913 0.01346 1.092 0.00775 1.62 0.01404
AFILE
mh114.dat

! Section 1
SECTION
!Xle    Yle    Zle    Chord    Ainc
0    0.26875    0.0   0.1875    0.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Aileron 1.0 0.75 0.0 0.0 0.0 -1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Canard 1.0 0.75 0.0 0.0 0.0 1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Tilt 1.0 0.0 0.0 0.0 0.0 1.0
!mh114.dat at Re = 200000
CLAF
1.0
CDCL
0.3913 0.01346 1.092 0.00775 1.62 0.01404
AFILE
mh114.dat


! Section 2
SECTION
!Xle    Yle    Zle    Chord    Ainc
0    0.75    0.0   0.170    0.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Aileron 1.0 0.75 0.0 0.0 0.0 -1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Canard 1.0 0.75 0.0 0.0 0.0 1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Tilt 1.0 0.0 0.0 0.0 0.0 1.0
!mh114.dat at Re = 200000
CLAF
1.0
CDCL
0.3913 0.01346 1.092 0.00775 1.62 0.01404
AFILE
mh114.dat



!!!!!!!!!!!!!!!!!!!!!!!! Rear Wing
SURFACE
2 (Rear Wing)
!Nchordwise  Cspace    Nspanwise   Sspace
10   1.0   40   1.0
YDUPLICATE
0.0
TRANSLATE
%(rw_trans)s
!----------------------------------
! Section 0
SECTION
!Xle    Yle    Zle    Chord    Ainc
0    0    0   0.1875    2.2
!mh114.dat at Re = 200000
CLAF
1.0
CDCL
0.3913 0.01346 1.092 0.00775 1.62 0.01404
AFILE
mh114.dat

! Section 1
SECTION
!Xle    Yle    Zle    Chord    Ainc
0    0.26875    0.0   0.1875    2.2
CONTROL
!Name gain Xhinge XYZhvec SignDup
Aileron 1.0 0.75 0.0 0.0 0.0 -1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Flap 1.0 0.75 0.0 0.0 0.0 1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Tilt 1.0 0.0 0.0 0.0 0.0 1.0
!mh114.dat at Re = 200000
CLAF
1.0
CDCL
0.3913 0.01346 1.092 0.00775 1.62 0.01404
AFILE
mh114.dat

! Section 2
SECTION
!Xle    Yle    Zle    Chord    Ainc
0    0.75    0.0   0.170    2.2
CONTROL
!Name gain Xhinge XYZhvec SignDup
Aileron 1.0 0.75 0.0 0.0 0.0 -1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Flap 1.0 0.75 0.0 0.0 0.0 1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Tilt 1.0 0.0 0.0 0.0 0.0 1.0
!mh114.dat at Re = 200000
CLAF
1.0
CDCL
0.3913 0.01346 1.092 0.00775 1.62 0.01404
AFILE
mh114.dat

!!Fuselage
BODY
Fuselage
20	1.0
SCALE
1.625 1.625 1.625
TRANSLATE
-0.754 0.0  0.0885
BFILE
PT1_fuse_2012_03_14.dat



SURFACE
3 (V-tail)
!Nchordwise  Cspace    Nspanwise   Sspace
10   1.0   30   1.0
YDUPLICATE
0.0
SCALE 
1.0 1.0 1.0
TRANSLATE
0.5628     0.0     0.09
!----------------------------------
! Section 0
SECTION
!Xle    Yle    Zle    Chord    Ainc
0.0    0.0    0.0   0.25    0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Elevator 1.0 0.75 0.0 0.0 0.0 1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Rudder 1.0 0.75 0.0 0.0 0.0 -1.0
!naca15412n.dat at Re = 160K 
CLAF
1.0
CDCL
-0.95 0.0091 -0.5238 0.00497 0.5975 0.0150
AFILE
naca15412n.dat
!&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
! Section 1
SECTION
!Xle    Yle    Zle    Chord    Ainc
0.2935    0.39675    -0.2188   0.125    0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Elevator 1.0 0.75 0.0 0.0 0.0 1.0
CONTROL
!Name gain Xhinge XYZhvec SignDup
Rudder 1.0 0.75 0.0 0.0 0.0 -1.0
!naca15412n.dat at Re = 160K 
CLAF
1.0
CDCL
-0.95 0.0091 -0.5238 0.00497 0.5975 0.0150
AFILE
naca15412n.dat
!&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&




!!Copyright 2012, Pranay Sinha, Transition Robotics, Inc.
"""
