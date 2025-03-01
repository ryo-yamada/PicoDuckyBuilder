import sys
if sys.platform == "win32":
    from windows import main
    main()
elif sys.platform == "linux":
    from linux import main
    main()
elif sys.platform == "darwin":
    from macos import main
    main()