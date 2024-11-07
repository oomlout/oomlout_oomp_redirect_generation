import os


def main(**kwargs):
    import action_build_oomp
    action_build_oomp.main(**kwargs)
    import action_build_redirect
    action_build_redirect.main(**kwargs)
    import action_redirect_upload
    action_redirect_upload.main(**kwargs)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)