import apiRepository

print(apiRepository.getGroups().json())
print(apiRepository.setBrightnessToGroup(1, 255).json())
print('done!')