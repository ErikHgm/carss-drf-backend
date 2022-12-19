# API Testing

## TOC
  - [Testing Endpoints](#testing-endpoints)
  - [Testing CRUD Functionality](#testing-crud-functionality)
    - [Save App](#save-app)
    - [Followers App](#followers-app)
    - [Profiles App](#profiles-app)
    - [Cars App](#cars-app)
- [Validating Code](#validating-code)


Manual testing took place throughout development of the API to ensure features functioned. These included visiting each URL to ensure accurate results were returned depending on authorization state, the creation, update and deletion of items:

### Testing Endpoints

| URL | Passed |
|---|---|
| root | :white_check_mark: |
| /saved/ | :white_check_mark: |
| /saved/\<id>/ | :white_check_mark: |
| /followers/ | :white_check_mark: |
| /followers/\<id>/ | :white_check_mark: |
| /profiles/ | :white_check_mark: |
| /profiles/\<id>/ | :white_check_mark: |
| /cars/ | :white_check_mark: |
| /cars/create | :white_check_mark: |
| /cars/\<id>/ | :white_check_mark: |

### Testing CRUD Functionality

#### Save App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Save | Read (List) | Array of owned objects | 403 Response | :white_check_mark: |
| Save | Read - Valid ID and Owner | Returns Detail | 404 Response | :white_check_mark: |
| Save | Read - Valid ID and not Owner | 404 Response | 404 Response | :white_check_mark: |
| Save | Read - Invalid ID | 404 Response | 404 Response  | :white_check_mark: |
| Save | Create | 201 Response | N/A | :white_check_mark: |
| Save | Update | N/A| N/A | N/A |
| Save | Delete | 204 Response | N/A | :white_check_mark: |

#### Followers App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Followers | Read (List) | Array of owned objects | Empty Results Array | :white_check_mark: |
| Followers | Read - Valid ID and Owner | Returns Detail | 403 Response | :white_check_mark: |
| Followers | Read - Valid ID and not Owner | 404 Response | 404 Response | :white_check_mark: |
| Followers | Read - Invalid ID | 404 Response | 404 Response  | :white_check_mark: |
| Followers | Create | 201 Response | N/A | :white_check_mark: |
| Followers | Update | N/A | N/A | N/A |
| Followers | Delete | 204 Response | N/A | :white_check_mark: |

#### Profiles App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Profiles | Read (List) | Array of profiles | Array of profiles | :white_check_mark: |
| Profiles | Read | Returns Detail | Returns Detail | :white_check_mark: |
| Profiles | Create | N/A | N/A | N/A |
| Profiles | Update | 200 Response | N/A | :white_check_mark: |

#### Cars App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Cars | Read (List) | Array of all cars | Array of all cars | :white_check_mark: |
| Cars | Read | Returns Detail | Returns Detail | :white_check_mark: |
| Cars | Create | 201 Response | N/A | :white_check_mark: |
| Cars | Update | 200 Response | N/A | :white_check_mark: |
| Cars | Delete | 204 Response | N/A | :white_check_mark: |

## Validating Code

The `pycodestyle` package was used throughout the development of the project to validate and fix problems in the code continuously. No validation errors were present in the final deployed version.