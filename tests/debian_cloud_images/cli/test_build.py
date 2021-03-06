from debian_cloud_images.cli.build import (
    ArchEnum,
    ReleaseEnum,
)


class TestCommand:
    def test_check(self):
        stretch = ReleaseEnum.stretch
        sid = ReleaseEnum.sid
        amd64 = ArchEnum.amd64
        arm64 = ArchEnum.arm64

        assert sid.supports_linux_image_cloud_for_arch(amd64.name) is True
        assert sid.supports_linux_image_cloud_for_arch(arm64.name) is False
        assert stretch.supports_linux_image_cloud_for_arch(arm64.name) is False
