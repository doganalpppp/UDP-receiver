from conans import ConanFile, Meson

class conanIntegrator(ConanFile):
    name = "new_reciever"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"
    #for gcc
    requires = "boost/1.73.0"
    exports_sources = "src/*"

    def source(self):
        self.output.success("Formatting .cpp and .hpp files ...")
        self.run("ninja -C ../build clang-format")
        self.output.success("Formatting .cpp and .hpp files completed.")  

    def build(self):
        meson = Meson(self)
        meson.configure(source_folder="%s" % self.source_folder,
                        build_folder="%s/build" % self.source_folder)
        meson.build()

    def package(self):
        self.copy("siu-vsm-bridge", dst="bin", keep_path=False)