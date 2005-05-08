builtins = (
  'A_CORRELATE',
  'ABS',
  'ACOS',
  'ADAPT_HIST_EQUAL',
  'ALOG',
  'ALOG10',
  'AMOEBA',
  'ANNOTATE',
  'APP_USER_DIR',
  'APP_USER_DIR_QUERY',
  'ARG_PRESENT',
  'ARRAY_EQUAL',
  'ARRAY_INDICES',
  'ARROW',
  'ASCII_TEMPLATE',
  'ASIN',
  'ASSOC',
  'ATAN',
  'AXIS',
  'BAR_PLOT',
  'BESELI',
  'BESELJ',
  'BESELK',
  'BESELY',
  'BETA',
  'BILINEAR',
  'BIN_DATE',
  'BINARY_TEMPLATE',
  'BINDGEN',
  'BINOMIAL',
  'BLAS_AXPY',
  'BLK_CON',
  'BOX_CURSOR',
  'BREAKPOINT',
  'BROYDEN',
  'BYTARR',
  'BYTE',
  'BYTEORDER',
  'BYTSCL',
  'C_CORRELATE',
  'CALDAT',
  'CALENDAR',
  'CALL_EXTERNAL',
  'CALL_FUNCTION',
  'CALL_METHOD',
  'CALL_PROCEDURE',
  'CATCH',
  'CD',
  'CDF_ATTCREATE',
  'CDF_ATTDELETE',
  'CDF_ATTEXISTS',
  'CDF_ATTGET',
  'CDF_ATTINQ',
  'CDF_ATTNUM',
  'CDF_ATTPUT',
  'CDF_ATTRENAME',
  'CDF_CLOSE',
  'CDF_COMPRESSION',
  'CDF_CONTROL',
  'CDF_CREATE',
  'CDF_DELETE',
  'CDF_DOC',
  'CDF_ENCODE_EPOCH',
  'CDF_EPOCH',
  'CDF_ERROR',
  'CDF_EXISTS',
  'CDF_INQUIRE',
  'CDF_LIB_INFO',
  'CDF_OPEN',
  'CDF_PARSE_EPOCH',
  'CDF_VARCREATE',
  'CDF_VARDELETE',
  'CDF_VARGET',
  'CDF_VARGET1',
  'CDF_VARINQ',
  'CDF_VARNUM',
  'CDF_VARPUT',
  'CDF_VARRENAME',
  'CEIL',
  'CHEBYSHEV',
  'CHECK_MATH',
  'CHISQR_CVF',
  'CHISQR_PDF',
  'CHOLDC',
  'CHOLSOL',
  'CINDGEN',
  'CIR_3PNT',
  'CLOSE',
  'CLUST_WTS',
  'CLUSTER',
  'CLUSTER_TREE',
  'COLOR_CONVERT',
  'COLOR_QUAN',
  'COLORMAP_APPLICABLE',
  'COMFIT',
  'COMPLEX',
  'COMPLEXARR',
  'COMPLEXROUND',
  'COMPUTE_MESH_NORMALS',
  'COND',
  'CONGRID',
  'CONJ',
  'CONSTRAINED_MIN',
  'CONTOUR',
  'CONVERT_COORD',
  'CONVOL',
  'COORD2TO3',
  'COPY_LUN',
  'CORRELATE',
  'COS',
  'COSH',
  'CPU',
  'CRAMER',
  'CREATE_CURSOR',
  'CREATE_STRUCT',
  'CREATE_VIEW',
  'CROSSP',
  'CRVLENGTH',
  'CT_LUMINANCE',
  'CTI_TEST',
  'CURSOR',
  'CURVEFIT',
  'CV_COORD',
  'CVTTOBM',
  'CW_ANIMATE',
  'CW_ANIMATE_GETP',
  'CW_ANIMATE_LOAD',
  'CW_ANIMATE_RUN',
  'CW_ARCBALL',
  'CW_BGROUP',
  'CW_CLR_INDEX',
  'CW_COLORSEL',
  'CW_DEFROI',
  'CW_FIELD',
  'CW_FILESEL',
  'CW_FORM',
  'CW_FSLIDER',
  'CW_LIGHT_EDITOR',
  'CW_LIGHT_EDITOR_GET',
  'CW_LIGHT_EDITOR_SET',
  'CW_ORIENT',
  'CW_PALETTE_EDITOR',
  'CW_PALETTE_EDITOR_GET',
  'CW_PALETTE_EDITOR_SET',
  'CW_PDMENU',
  'CW_RGBSLIDER',
  'CW_TMPL',
  'CW_ZOOM',
  'DBLARR',
  'DCINDGEN',
  'DCOMPLEX',
  'DCOMPLEXARR',
  'DEFINE_KEY',
  'DEFINE_MSGBLK',
  'DEFINE_MSGBLK_FROM_FILE',
  'DEFROI',
  'DEFSYSV',
  'DELVAR',
  'DENDRO_PLOT',
  'DENDROGRAM',
  'DERIV',
  'DERIVSIG',
  'DETERM',
  'DEVICE',
  'DFPMIN',
  'DIAG_MATRIX',
  'DIALOG_MESSAGE',
  'DIALOG_PICKFILE',
  'DIALOG_PRINTERSETUP',
  'DIALOG_PRINTJOB',
  'DIALOG_READ_IMAGE',
  'DIALOG_WRITE_IMAGE',
  'DIGITAL_FILTER',
  'DILATE',
  'DINDGEN',
  'DISSOLVE',
  'DIST',
  'DISTANCE_MEASURE',
  'DLM_LOAD',
  'DLM_REGISTER',
  'DOC_LIBRARY',
  'DOUBLE',
  'DRAW_ROI',
  'EFONT',
  'EIGENQL',
  'EIGENVEC',
  'ELMHES',
  'EMPTY',
  'ENABLE_SYSRTN',
  'EOF',
  'EOS_EH_CONVANG',
  'EOS_EH_GETVERSION',
  'EOS_EH_IDINFO',
  'EOS_EXISTS',
  'EOS_GD_ATTACH',
  'EOS_GD_ATTRINFO',
  'EOS_GD_BLKSOMOFFSET',
  'EOS_GD_CLOSE',
  'EOS_GD_COMPINFO',
  'EOS_GD_CREATE',
  'EOS_GD_DEFBOXREGION',
  'EOS_GD_DEFCOMP',
  'EOS_GD_DEFDIM',
  'EOS_GD_DEFFIELD',
  'EOS_GD_DEFORIGIN',
  'EOS_GD_DEFPIXREG',
  'EOS_GD_DEFPROJ',
  'EOS_GD_DEFTILE',
  'EOS_GD_DEFVRTREGION',
  'EOS_GD_DETACH',
  'EOS_GD_DIMINFO',
  'EOS_GD_DUPREGION',
  'EOS_GD_EXTRACTREGION',
  'EOS_GD_FIELDINFO',
  'EOS_GD_GETFILLVALUE',
  'EOS_GD_GETPIXELS',
  'EOS_GD_GETPIXVALUES',
  'EOS_GD_GRIDINFO',
  'EOS_GD_INQATTRS',
  'EOS_GD_INQDIMS',
  'EOS_GD_INQFIELDS',
  'EOS_GD_INQGRID',
  'EOS_GD_INTERPOLATE',
  'EOS_GD_NENTRIES',
  'EOS_GD_OPEN',
  'EOS_GD_ORIGININFO',
  'EOS_GD_PIXREGINFO',
  'EOS_GD_PROJINFO',
  'EOS_GD_QUERY',
  'EOS_GD_READATTR',
  'EOS_GD_READFIELD',
  'EOS_GD_READTILE',
  'EOS_GD_REGIONINFO',
  'EOS_GD_SETFILLVALUE',
  'EOS_GD_SETTILECACHE',
  'EOS_GD_TILEINFO',
  'EOS_GD_WRITEATTR',
  'EOS_GD_WRITEFIELD',
  'EOS_GD_WRITEFIELDMETA',
  'EOS_GD_WRITETILE',
  'EOS_PT_ATTACH',
  'EOS_PT_ATTRINFO',
  'EOS_PT_BCKLINKINFO',
  'EOS_PT_CLOSE',
  'EOS_PT_CREATE',
  'EOS_PT_DEFBOXREGION',
  'EOS_PT_DEFLEVEL',
  'EOS_PT_DEFLINKAGE',
  'EOS_PT_DEFTIMEPERIOD',
  'EOS_PT_DEFVRTREGION',
  'EOS_PT_DETACH',
  'EOS_PT_EXTRACTPERIOD',
  'EOS_PT_EXTRACTREGION',
  'EOS_PT_FWDLINKINFO',
  'EOS_PT_GETLEVELNAME',
  'EOS_PT_GETRECNUMS',
  'EOS_PT_INQATTRS',
  'EOS_PT_INQPOINT',
  'EOS_PT_LEVELINDX',
  'EOS_PT_LEVELINFO',
  'EOS_PT_NFIELDS',
  'EOS_PT_NLEVELS',
  'EOS_PT_NRECS',
  'EOS_PT_OPEN',
  'EOS_PT_PERIODINFO',
  'EOS_PT_PERIODRECS',
  'EOS_PT_QUERY',
  'EOS_PT_READATTR',
  'EOS_PT_READLEVEL',
  'EOS_PT_REGIONINFO',
  'EOS_PT_REGIONRECS',
  'EOS_PT_SIZEOF',
  'EOS_PT_UPDATELEVEL',
  'EOS_PT_WRITEATTR',
  'EOS_PT_WRITELEVEL',
  'EOS_QUERY',
  'EOS_SW_ATTACH',
  'EOS_SW_ATTRINFO',
  'EOS_SW_CLOSE',
  'EOS_SW_COMPINFO',
  'EOS_SW_DEFBOXREGION',
  'EOS_SW_DEFBOXREGION',
  'EOS_SW_DEFCOMP',
  'EOS_SW_DEFDATAFIELD',
  'EOS_SW_DEFDIM',
  'EOS_SW_DEFDIMMAP',
  'EOS_SW_DEFGEOFIELD',
  'EOS_SW_DEFIDXMAP',
  'EOS_SW_DEFTIMEPERIOD',
  'EOS_SW_DEFVRTREGION',
  'EOS_SW_DETACH',
  'EOS_SW_DIMINFO',
  'EOS_SW_DUPREGION',
  'EOS_SW_EXTRACTPERIOD',
  'EOS_SW_EXTRACTREGION',
  'EOS_SW_FIELDINFO',
  'EOS_SW_GETFILLVALUE',
  'EOS_SW_IDXMAPINFO',
  'EOS_SW_INQATTRS',
  'EOS_SW_INQDATAFIELDS',
  'EOS_SW_INQDIMS',
  'EOS_SW_INQGEOFIELDS',
  'EOS_SW_INQIDXMAPS',
  'EOS_SW_INQMAPS',
  'EOS_SW_INQSWATH',
  'EOS_SW_MAPINFO',
  'EOS_SW_NENTRIES',
  'EOS_SW_OPEN',
  'EOS_SW_PERIODINFO',
  'EOS_SW_QUERY',
  'EOS_SW_READATTR',
  'EOS_SW_READFIELD',
  'EOS_SW_REGIONINFO',
  'EOS_SW_SETFILLVALUE',
  'EOS_SW_WRITEATTR',
  'EOS_SW_WRITEDATAMETA',
  'EOS_SW_WRITEFIELD',
  'EOS_SW_WRITEGEOMETA',
  'ERASE',
  'ERF',
  'ERFC',
  'ERFCX',
  'ERODE',
  'ERRPLOT',
  'EXECUTE',
  'EXIT',
  'EXP',
  'EXPAND',
  'EXPAND_PATH',
  'EXPINT',
  'EXTRAC',
  'EXTRACT_SLICE',
  'F_CVF',
  'F_PDF',
  'FACTORIAL',
  'FFT',
  'FILE_BASENAME',
  'FILE_CHMOD',
  'FILE_COPY',
  'FILE_DELETE',
  'FILE_DIRNAME',
  'FILE_EXPAND_PATH',
  'FILE_INFO',
  'FILE_LINES',
  'FILE_LINK',
  'FILE_MKDIR',
  'FILE_MOVE',
  'FILE_READLINK',
  'FILE_SAME',
  'FILE_SEARCH',
  'FILE_TEST',
  'FILE_WHICH',
  'FILEPATH',
  'FINDGEN',
  'FINITE',
  'FIX',
  'FLICK',
  'FLOAT',
  'FLOOR',
  'FLOW3',
  'FLTARR',
  'FLUSH',
  'FORMAT_AXIS_VALUES',
  'FREE_LUN',
  'FSTAT',
  'FULSTR',
  'FUNCT',
  'FV_TEST',
  'FX_ROOT',
  'FZ_ROOTS',
  'GAMMA',
  'GAMMA_CT',
  'GAUSS_CVF',
  'GAUSS_PDF',
  'GAUSS2DFIT',
  'GAUSSFIT',
  'GAUSSINT',
  'GET_DRIVE_LIST',
  'GET_KBRD',
  'GET_LUN',
  'GET_SCREEN_SIZE',
  'GETENV',
  'GRID_INPUT',
  'GRID_TPS',
  'GRID3',
  'GRIDDATA',
  'GS_ITER',
  'H_EQ_CT',
  'H_EQ_INT',
  'H5_CLOSE',
  'H5_GET_LIBVERSION',
  'H5_OPEN',
  'H5_PARSE',
  'H5A_CLOSE',
  'H5A_GET_NAME',
  'H5A_GET_NUM_ATTRS',
  'H5A_GET_SPACE',
  'H5A_GET_TYPE',
  'H5A_OPEN_IDX',
  'H5A_OPEN_NAME',
  'H5A_READ',
  'H5D_CLOSE',
  'H5D_GET_SPACE',
  'H5D_GET_STORAGE_SIZE',
  'H5D_GET_TYPE',
  'H5D_OPEN',
  'H5D_READ',
  'H5F_CLOSE',
  'H5F_IS_HDF5',
  'H5F_OPEN',
  'H5G_CLOSE',
  'H5G_GET_COMMENT',
  'H5G_GET_LINKVAL',
  'H5G_GET_MEMBER_NAME',
  'H5G_GET_NMEMBERS',
  'H5G_GET_OBJINFO',
  'H5G_OPEN',
  'H5I_GET_TYPE',
  'H5R_DEREFERENCE',
  'H5R_GET_OBJECT_TYPE',
  'H5S_CLOSE',
  'H5S_COPY',
  'H5S_CREATE_SIMPLE',
  'H5S_GET_SELECT_BOUNDS',
  'H5S_GET_SELECT_ELEM_NPOINTS',
  'H5S_GET_SELECT_ELEM_POINTLIST',
  'H5S_GET_SELECT_HYPER_BLOCKLIST',
  'H5S_GET_SELECT_HYPER_NBLOCKS',
  'H5S_GET_SELECT_NPOINTS',
  'H5S_GET_SIMPLE_EXTENT_DIMS',
  'H5S_GET_SIMPLE_EXTENT_NDIMS',
  'H5S_GET_SIMPLE_EXTENT_NPOINTS',
  'H5S_GET_SIMPLE_EXTENT_TYPE',
  'H5S_IS_SIMPLE',
  'H5S_OFFSET_SIMPLE',
  'H5S_SELECT_ALL',
  'H5S_SELECT_ELEMENTS',
  'H5S_SELECT_HYPERSLAB',
  'H5S_SELECT_NONE',
  'H5S_SELECT_VALID',
  'H5T_CLOSE',
  'H5T_COMMITTED',
  'H5T_COPY',
  'H5T_EQUAL',
  'H5T_GET_ARRAY_DIMS',
  'H5T_GET_ARRAY_NDIMS',
  'H5T_GET_CLASS',
  'H5T_GET_CSET',
  'H5T_GET_EBIAS',
  'H5T_GET_FIELDS',
  'H5T_GET_INPAD',
  'H5T_GET_MEMBER_CLASS',
  'H5T_GET_MEMBER_NAME',
  'H5T_GET_MEMBER_OFFSET',
  'H5T_GET_MEMBER_TYPE',
  'H5T_GET_NMEMBERS',
  'H5T_GET_NORM',
  'H5T_GET_OFFSET',
  'H5T_GET_ORDER',
  'H5T_GET_PAD',
  'H5T_GET_PRECISION',
  'H5T_GET_SIGN',
  'H5T_GET_SIZE',
  'H5T_GET_STRPAD',
  'H5T_GET_SUPER',
  'H5T_IDLTYPE',
  'H5T_MEMTYPE',
  'H5T_OPEN',
  'H5_BROWSER',
  'HANNING',
  'HDF_AN_ANNLEN',
  'HDF_AN_ANNLIST',
  'HDF_AN_ATYPE2TAG',
  'HDF_AN_CREATE',
  'HDF_AN_CREATEF',
  'HDF_AN_END',
  'HDF_AN_ENDACCESS',
  'HDF_AN_FILEINFO',
  'HDF_AN_GET_TAGREF',
  'HDF_Annotation_id2TAGREF',
  'HDF_AN_NUMANN',
  'HDF_AN_READANN',
  'HDF_AN_SELECT',
  'HDF_AN_START',
  'HDF_Annotation_tag2ATYPE',
  'HDF_Annotation_tagREF2ID',
  'HDF_AN_WRITEANN',
  'HDF_BROWSER',
  'HDF_CLOSE',
  'HDF_DELDD',
  'HDF_DF24_ADDIMAGE',
  'HDF_DF24_GETIMAGE',
  'HDF_DF24_GETINFO',
  'HDF_DF24_LASTREF',
  'HDF_DF24_NIMAGES',
  'HDF_DF24_READREF',
  'HDF_DF24_RESTART',
  'HDF_DFAN_ADDFDS',
  'HDF_DFAN_ADDFID',
  'HDF_DFAN_GETDESC',
  'HDF_DFAN_GETFDS',
  'HDF_DFAN_GETFID',
  'HDF_DFAN_GETLABEL',
  'HDF_DFAN_LABLIST',
  'HDF_DFAN_LASTREF',
  'HDF_DFAN_PUTDESC',
  'HDF_DFAN_PUTLABEL',
  'HDF_DFP_ADDPAL',
  'HDF_DFP_GETPAL',
  'HDF_DFP_LASTREF',
  'HDF_DFP_NPALS',
  'HDF_DFP_PUTPAL',
  'HDF_DFP_READREF',
  'HDF_DFP_RESTART',
  'HDF_DFP_WRITEREF',
  'HDF_DFR8_ADDIMAGE',
  'HDF_DFR8_GETIMAGE',
  'HDF_DFR8_GETINFO',
  'HDF_DFR8_LASTREF',
  'HDF_DFR8_NIMAGES',
  'HDF_DFR8_PUTIMAGE',
  'HDF_DFR8_READREF',
  'HDF_DFR8_RESTART',
  'HDF_DFR8_SETPALETTE',
  'HDF_DUPDD',
  'HDF_EXISTS',
  'HDF_GR_ATTRINFO',
  'HDF_GR_CREATE',
  'HDF_GR_END',
  'HDF_GR_ENDACCESS',
  'HDF_GR_FILEINFO',
  'HDF_GR_FINDATTR',
  'HDF_GR_GETATTR',
  'HDF_GR_GETCHUNKINFO',
  'HDF_GR_GETIMINFO',
  'HDF_GR_GETLUTID',
  'HDF_GR_GETLUTINFO',
  'HDF_GR_IDTOREF',
  'HDF_GR_LUTTOREF',
  'HDF_GR_NAMETOINDEX',
  'HDF_GR_READIMAGE',
  'HDF_GR_READLUT',
  'HDF_GR_REFTOINDEX',
  'HDF_GR_SELECT',
  'HDF_GR_SETATTR',
  'HDF_GR_SETCHUNK',
  'HDF_GR_SETCHUNKCACHE',
  'HDF_GR_SETCOMPRESS',
  'HDF_GR_SETEXTERNALFILE',
  'HDF_GR_START',
  'HDF_GR_WRITEIMAGE',
  'HDF_GR_WRITELUT',
  'HDF_HDF2IDLTYPE',
  'HDF_IDL2HDFTYPE',
  'HDF_ISHDF',
  'HDF_LIB_INFO',
  'HDF_NEWREF',
  'HDF_NUMBER',
  'HDF_OPEN',
  'HDF_PACKDATA',
  'HDF_READ',
  'HDF_SD_ADDDATA',
  'HDF_SD_ATTRFIND',
  'HDF_SD_ATTRINFO',
  'HDF_SD_ATTRSET',
  'HDF_SD_CREATE',
  'HDF_SD_DIMGET',
  'HDF_SD_DIMGETID',
  'HDF_SD_DIMSET',
  'HDF_SD_END',
  'HDF_SD_ENDACCESS',
  'HDF_SD_FILEINFO',
  'HDF_SD_GETDATA',
  'HDF_SD_GETINFO',
  'HDF_SDinterface_idTOREF',
  'HDF_SD_ISCOORDVAR',
  'HDF_SD_NAMETOINDEX',
  'HDF_SD_REFTOINDEX',
  'HDF_SD_SELECT',
  'HDF_SD_SETCOMPRESS',
  'HDF_SD_SETEXTFILE',
  'HDF_SD_SETINFO',
  'HDF_SD_START',
  'HDF_UNPACKDATA',
  'HDF_VD_ATTACH',
  'HDF_VD_ATTRFIND',
  'HDF_VD_ATTRINFO',
  'HDF_VD_ATTRSET',
  'HDF_VD_DETACH',
  'HDF_VD_FDEFINE',
  'HDF_VD_FEXIST',
  'HDF_VD_FIND',
  'HDF_VD_GET',
  'HDF_VD_GETID',
  'HDF_VD_GETINFO',
  'HDF_VD_INSERT',
  'HDF_VD_ISATTR',
  'HDF_VD_ISVD',
  'HDF_VD_ISVG',
  'HDF_VD_LONE',
  'HDF_VD_NATTRS',
  'HDF_VD_READ',
  'HDF_VD_SEEK',
  'HDF_VD_SETINFO',
  'HDF_VD_WRITE',
  'HDF_VG_ADDTR',
  'HDF_VG_ATTACH',
  'HDF_VG_DETACH',
  'HDF_VG_GETID',
  'HDF_VG_GETINFO',
  'HDF_VG_GETNEXT',
  'HDF_VG_GETTR',
  'HDF_VG_GETTRS',
  'HDF_VG_INQTR',
  'HDF_VG_INSERT',
  'HDF_VG_ISVD',
  'HDF_VG_ISVG',
  'HDF_VG_LONE',
  'HDF_VG_NUMBER',
  'HDF_VG_SETINFO',
  'HDF_BROWSER',
  'HDF_READ',
  'HEAP_FREE',
  'HEAP_GC',
  'HELP',
  'HILBERT',
  'HIST_2D',
  'HIST_EQUAL',
  'HISTOGRAM',
  'HLS',
  'HOUGH',
  'HQR',
  'HSV',
  'IBETA',
  'ICONTOUR',
  'IDENTITY',
  'IDL_VALIDNAME',
  'IDLITSYS_CREATETOOL',
  'IGAMMA',
  'IIMAGE',
  'IMAGE_CONT',
  'IMAGE_STATISTICS',
  'IMAGINARY',
  'IMAP',
  'INDGEN',
  'INT_2D',
  'INT_3D',
  'INT_TABULATED',
  'INTARR',
  'INTERPOL',
  'INTERPOLATE',
  'INTERVAL_VOLUME',
  'INVERT',
  'IOCTL',
  'IPLOT',
  'ISHFT',
  'ISOCONTOUR',
  'ISOSURFACE',
  'ISURFACE',
  'ITCURRENT',
  'ITDELETE',
  'ITGETCURRENT',
  'ITREGISTER',
  'ITRESET',
  'ITRESOLVE',
  'IVOLUME',
  'JOURNAL',
  'JULDAY',
  'KEYWORD_SET',
  'KRIG2D',
  'KURTOSIS',
  'KW_TEST',
  'L64INDGEN',
  'LA_CHOLDC',
  'LA_CHOLMPROVE',
  'LA_CHOLSOL',
  'LA_DETERM',
  'LA_EIGENPROBLEM',
  'LA_EIGENQL',
  'LA_EIGENVEC',
  'LA_ELMHES',
  'LA_GM_LINEAR_MODEL',
  'LA_HQR',
  'LA_INVERT',
  'LA_LEAST_SQUARE_EQUALITY',
  'LA_LEAST_SQUARES',
  'LA_LINEAR_EQUATION',
  'LA_LUDC',
  'LA_LUMPROVE',
  'LA_LUSOL',
  'LA_SVD',
  'LA_TRIDC',
  'LA_TRIMPROVE',
  'LA_TRIQL',
  'LA_TRIRED',
  'LA_TRISOL',
  'LABEL_DATE',
  'LABEL_REGION',
  'LADFIT',
  'LAGUERRE',
  'LEEFILT',
  'LEGENDRE',
  'LINBCG',
  'LINDGEN',
  'LINFIT',
  'LINKIMAGE',
  'LL_ARC_DISTANCE',
  'LMFIT',
  'LMGR',
  'LNGAMMA',
  'LNP_TEST',
  'LOADCT',
  'LOCALE_GET',
  'LOGICAL_AND',
  'LOGICAL_OR',
  'LOGICAL_TRUE',
  'LON64ARR',
  'LONARR',
  'LONG',
  'LONG64',
  'LSODE',
  'LU_COMPLEX',
  'LUDC',
  'LUMPROVE',
  'LUSOL',
  'M_CORRELATE',
  'MACHAR',
  'MAKE_ARRAY',
  'MAKE_DLL',
  'MAP_2POINTS',
  'MAP_CONTINENTS',
  'MAP_GRID',
  'MAP_IMAGE',
  'MAP_PATCH',
  'MAP_PROJ_FORWARD',
  'MAP_PROJ_IMAGE',
  'MAP_PROJ_INFO',
  'MAP_PROJ_INIT',
  'MAP_PROJ_INVERSE',
  'MAP_SET',
  'MATRIX_MULTIPLY',
  'MATRIX_POWER',
  'MAX',
  'MD_TEST',
  'MEAN',
  'MEANABSDEV',
  'MEDIAN',
  'MEMORY',
  'MESH_CLIP',
  'MESH_DECIMATE',
  'MESH_ISSOLID',
  'MESH_MERGE',
  'MESH_NUMTRIANGLES',
  'MESH_OBJ',
  'MESH_SMOOTH',
  'MESH_SURFACEAREA',
  'MESH_VALIDATE',
  'MESH_VOLUME',
  'MESSAGE',
  'MIN',
  'MIN_CURVE_SURF',
  'MK_HTML_HELP',
  'MODIFYCT',
  'MOMENT',
  'MORPH_CLOSE',
  'MORPH_DISTANCE',
  'MORPH_GRADIENT',
  'MORPH_HITORMISS',
  'MORPH_OPEN',
  'MORPH_THIN',
  'MORPH_TOPHAT',
  'MPEG_CLOSE',
  'MPEG_OPEN',
  'MPEG_PUT',
  'MPEG_SAVE',
  'MULTI',
  'N_ELEMENTS',
  'N_PARAMS',
  'N_TAGS',
  'NCDF_ATTCOPY',
  'NCDF_ATTDEL',
  'NCDF_ATTGET',
  'NCDF_ATTINQ',
  'NCDF_ATTNAME',
  'NCDF_ATTPUT',
  'NCDF_ATTRENAME',
  'NCDF_CLOSE',
  'NCDF_CONTROL',
  'NCDF_CREATE',
  'NCDF_DIMDEF',
  'NCDF_DIMID',
  'NCDF_DIMINQ',
  'NCDF_DIMRENAME',
  'NCDF_EXISTS',
  'NCDF_INQUIRE',
  'NCDF_OPEN',
  'NCDF_VARDEF',
  'NCDF_VARGET',
  'NCDF_VARID',
  'NCDF_VARINQ',
  'NCDF_VARPUT',
  'NCDF_VARRENAME',
  'NEWTON',
  'NORM',
  'OBJ_CLASS',
  'OBJ_DESTROY',
  'OBJ_ISA',
  'OBJ_NEW',
  'OBJ_VALID',
  'OBJARR',
  'ON_ERROR',
  'ONLINE_HELP',
  'ONLINE_HELP_PDF_INDEX',
  'OPEN',
  'OPLOT',
  'OPLOTERR',
  'P_CORRELATE',
  'PARTICLE_TRACE',
  'PATH_CACHE',
  'PATH_SEP',
  'PCOMP',
  'PLOT',
  'PLOT_3DBOX',
  'PLOT_FIELD',
  'PLOTERR',
  'PLOTS',
  'PNT_LINE',
  'POINT_LUN',
  'POLAR_CONTOUR',
  'POLAR_SURFACE',
  'POLY',
  'POLY_2D',
  'POLY_AREA',
  'POLY_FIT',
  'POLYFILL',
  'POLYFILLV',
  'POLYSHADE',
  'POLYWARP',
  'POPD',
  'POWELL',
  'PRIMES',
  'PRINT',
  'PRINTF',
  'PRINTD',
  'PRODUCT',
  'PROFILE',
  'PROFILER',
  'PROFILES',
  'PROJECT_VOL',
  'PS_SHOW_FONTS',
  'PSAFM',
  'PSEUDO',
  'PTR_FREE',
  'PTR_NEW',
  'PTR_VALID',
  'PTRARR',
  'PUSHD',
  'QGRID3',
  'QHULL',
  'QROMB',
  'QROMO',
  'QSIMP',
  'QUERY_BMP',
  'QUERY_DICOM',
  'QUERY_GIF',
  'QUERY_IMAGE',
  'QUERY_JPEG',
  'QUERY_JPEG2000',
  'QUERY_MRSID',
  'QUERY_PICT',
  'QUERY_PNG',
  'QUERY_PPM',
  'QUERY_SRF',
  'QUERY_TIFF',
  'QUERY_WAV',
  'R_CORRELATE',
  'R_TEST',
  'RADON',
  'RANDOMN',
  'RANDOMU',
  'RANKS',
  'RDPIX',
  'READ',
  'READF',
  'READ_ASCII',
  'READ_BINARY',
  'READ_BMP',
  'READ_DICOM',
  'READ_GIF',
  'READ_IMAGE',
  'READ_INTERFILE',
  'READ_JPEG',
  'READ_JPEG2000',
  'READ_MRSID',
  'READ_PICT',
  'READ_PNG',
  'READ_PPM',
  'READ_SPR',
  'READ_SRF',
  'READ_SYLK',
  'READ_TIFF',
  'READ_WAV',
  'READ_WAVE',
  'READ_X11_BITMAP',
  'READ_XWD',
  'READS',
  'READU',
  'REAL_PART',
  'REBIN',
  'RECALL_COMMANDS',
  'RECON3',
  'REDUCE_COLORS',
  'REFORM',
  'REGION_GROW',
  'REGISTER_CURSOR',
  'REGRESS',
  'REPLICATE',
  'REPLICATE_INPLACE',
  'RESOLVE_ALL',
  'RESOLVE_ROUTINE',
  'RESTORE',
  'RETALL',
  'RETURN',
  'REVERSE',
  'RK4',
  'ROBERTS',
  'ROT',
  'ROTATE',
  'ROUND',
  'ROUTINE_INFO',
  'RS_TEST',
  'S_TEST',
  'SAVE',
  'SAVGOL',
  'SCALE3',
  'SCALE3D',
  'SCOPE_LEVEL',
  'SCOPE_VARFETCH',
  'SCOPE_VARNAME',
  'SEARCH2D',
  'SEARCH3D',
  'SET_PLOT',
  'SET_SHADING',
  'SETENV',
  'SETUP_KEYS',
  'SFIT',
  'SHADE_SURF',
  'SHADE_SURF_IRR',
  'SHADE_VOLUME',
  'SHIFT',
  'SHMDEBUG',
  'SHMMAP',
  'SHMUNMAP',
  'SHMVAR',
  'SHOW3',
  'SHOWFONT',
  'SIMPLEX',
  'SIN',
  'SINDGEN',
  'SINH',
  'SIZE',
  'SKEWNESS',
  'SKIP_LUN',
  'SLICER3',
  'SLIDE_IMAGE',
  'SMOOTH',
  'SOBEL',
  'SOCKET',
  'SORT',
  'SPAWN',
  'SPH_4PNT',
  'SPH_SCAT',
  'SPHER_HARM',
  'SPL_INIT',
  'SPL_INTERP',
  'SPLINE',
  'SPLINE_P',
  'SPRSAB',
  'SPRSAX',
  'SPRSIN',
  'SPRSTP',
  'SQRT',
  'STANDARDIZE',
  'STDDEV',
  'STOP',
  'STRARR',
  'STRCMP',
  'STRCOMPRESS',
  'STREAMLINE',
  'STREGEX',
  'STRETCH',
  'STRING',
  'STRJOIN',
  'STRLEN',
  'STRLOWCASE',
  'STRMATCH',
  'STRMESSAGE',
  'STRMID',
  'STRPOS',
  'STRPUT',
  'STRSPLIT',
  'STRTRIM',
  'STRUCT_ASSIGN',
  'STRUCT_HIDE',
  'STRUPCASE',
  'SURFACE',
  'SURFR',
  'SVDC',
  'SVDFIT',
  'SVSOL',
  'SWAP_ENDIAN',
  'SWAP_ENDIAN_INPLACE',
  'SYSTIME',
  'T_CVF',
  'T_PDF',
  'T3D',
  'TAG_NAMES',
  'TAN',
  'TANH',
  'TEK_COLOR',
  'TEMPORARY',
  'TETRA_CLIP',
  'TETRA_SURFACE',
  'TETRA_VOLUME',
  'THIN',
  'THREED',
  'TIME_TEST2',
  'TIMEGEN',
  'TM_TEST',
  'TOTAL',
  'TRACE',
  'TRANSPOSE',
  'TRI_SURF',
  'TRIANGULATE',
  'TRIGRID',
  'TRIQL',
  'TRIRED',
  'TRISOL',
  'TRUNCATE_LUN',
  'TS_COEF',
  'TS_DIFF',
  'TS_FCAST',
  'TS_SMOOTH',
  'TV',
  'TVCRS',
  'TVLCT',
  'TVRD',
  'TVSCL',
  'UINDGEN',
  'UINT',
  'UINTARR',
  'UL64INDGEN',
  'ULINDGEN',
  'ULON64ARR',
  'ULONARR',
  'ULONG',
  'ULONG64',
  'UNIQ',
  'UNSHARP_MASK',
  'USERSYM',
  'VALUE_LOCATE',
  'VARIANCE',
  'VECTOR_FIELD',
  'VEL',
  'VELOVECT',
  'VERT_T3D',
  'VOIGT',
  'VORONOI',
  'VOXEL_PROJ',
  'WAIT',
  'WARP_TRI',
  'WATERSHED',
  'WDELETE',
  'WF_DRAW',
  'WHERE',
  'WIDGET_ACTIVEX',
  'WIDGET_BASE',
  'WIDGET_BUTTON',
  'WIDGET_COMBOBOX',
  'WIDGET_CONTROL',
  'WIDGET_DISPLAYCONTEXTMENU',
  'WIDGET_DRAW',
  'WIDGET_DROPLIST',
  'WIDGET_EVENT',
  'WIDGET_INFO',
  'WIDGET_LABEL',
  'WIDGET_LIST',
  'WIDGET_PROPERTYSHEET',
  'WIDGET_SLIDER',
  'WIDGET_TAB',
  'WIDGET_TABLE',
  'WIDGET_TEXT',
  'WIDGET_TREE',
  'WINDOW',
  'WRITE_BMP',
  'WRITE_GIF',
  'WRITE_IMAGE',
  'WRITE_JPEG',
  'WRITE_JPEG2000',
  'WRITE_NRIF',
  'WRITE_PICT',
  'WRITE_PNG',
  'WRITE_PPM',
  'WRITE_SPR',
  'WRITE_SRF',
  'WRITE_SYLK',
  'WRITE_TIFF',
  'WRITE_WAV',
  'WRITE_WAVE',
  'WRITEU',
  'WSET',
  'WSHOW',
  'WTN',
  'XBM_EDIT',
  'XDISPLAYFILE',
  'XDXF',
  'XFONT',
  'XINTERANIMATE',
  'XLOADCT',
  'XMANAGER',
  'XMNG_TMPL',
  'XMTOOL',
  'XOBJVIEW',
  'XOBJVIEW_ROTATE',
  'XOBJVIEW_WRITE_IMAGE',
  'XPALETTE',
  'XPCOLOR',
  'XPLOT3D',
  'XREGISTERED',
  'XROI',
  'XSQ_TEST',
  'XSURFACE',
  'XVAREDIT',
  'XVOLUME',
  'XVOLUME_ROTATE',
  'XVOLUME_WRITE_IMAGE',
  'XYOUTS',
  'ZOOM',
  'ZOOM_24',
)