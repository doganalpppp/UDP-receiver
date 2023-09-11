project(
    'new_reciever', 
    'cpp',
    version : '1.0.0',
    default_options : ['warning_level=1','cpp_std=c++17']
)

if meson.get_compiler('cpp').get_id() == 'clang'
  extra_args = ['-w','-MJ']
elif meson.get_compiler('cpp').get_id() == 'gcc'
  extra_args = ['-w', '-fcompare-debug-second']
endif

include_dir = include_directories(
    'include'  
    )

sources = [
    'src/main.cpp',
    'src/UDPClient.cpp' 
]

cpp = meson.get_compiler('cpp')


# outside dependencies
boost_dependency = dependency('boost', modules: ['thread', 'program_options', 'log', 'log_setup', 'filesystem', 'chrono', 'timer'])


dependencies = [
    boost_dependency
]

executable('UDP_reciever', sources, include_directories : include_dir, dependencies : dependencies, cpp_args :extra_args)
