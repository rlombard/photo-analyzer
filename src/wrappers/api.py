import requests
from typing import Optional, Dict, Any, List

class ImmichApi:
    def __init__(self, base_url: str = "/api", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    def _request(self, method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None, json: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.request(method, url, headers=self.headers, params=params, data=data, json=json)
        response.raise_for_status()
        return response.json() if response.content else None

    def getActivities(self, albumId: str, assetId: str, level: str, type: str, userId: str) -> Dict:
        return self._request("GET", "/activities")

    def createActivity(self, json_data: Dict) -> Dict:
        return self._request("POST", "/activities", json=json_data)

    def getActivityStatistics(self, albumId: str, assetId: str) -> Dict:
        return self._request("GET", "/activities/statistics")

    def deleteActivity(self, id: str) -> Dict:
        return self._request("DELETE", "/activities/{id}")

    def searchUsersAdmin(self, withDeleted: str) -> Dict:
        return self._request("GET", "/admin/users")

    def createUserAdmin(self, json_data: Dict) -> Dict:
        return self._request("POST", "/admin/users", json=json_data)

    def deleteUserAdmin(self, id: str, json_data: Dict) -> Dict:
        return self._request("DELETE", "/admin/users/{id}", json=json_data)

    def getUserAdmin(self, id: str) -> Dict:
        return self._request("GET", "/admin/users/{id}")

    def updateUserAdmin(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/admin/users/{id}", json=json_data)

    def getUserPreferencesAdmin(self, id: str) -> Dict:
        return self._request("GET", "/admin/users/{id}/preferences")

    def updateUserPreferencesAdmin(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/admin/users/{id}/preferences", json=json_data)

    def restoreUserAdmin(self, id: str) -> Dict:
        return self._request("POST", "/admin/users/{id}/restore")

    def getAllAlbums(self, assetId: str, shared: str) -> Dict:
        return self._request("GET", "/albums")

    def createAlbum(self, json_data: Dict) -> Dict:
        return self._request("POST", "/albums", json=json_data)

    def getAlbumStatistics(self) -> Dict:
        return self._request("GET", "/albums/statistics")

    def deleteAlbum(self, id: str) -> Dict:
        return self._request("DELETE", "/albums/{id}")

    def getAlbumInfo(self, id: str, key: str, withoutAssets: str) -> Dict:
        return self._request("GET", "/albums/{id}")

    def updateAlbumInfo(self, id: str, json_data: Dict) -> Dict:
        return self._request("PATCH", "/albums/{id}", json=json_data)

    def removeAssetFromAlbum(self, id: str, json_data: Dict) -> Dict:
        return self._request("DELETE", "/albums/{id}/assets", json=json_data)

    def addAssetsToAlbum(self, id: str, key: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/albums/{id}/assets", json=json_data)

    def removeUserFromAlbum(self, id: str, userId: str) -> Dict:
        return self._request("DELETE", "/albums/{id}/user/{userId}")

    def updateAlbumUser(self, id: str, userId: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/albums/{id}/user/{userId}", json=json_data)

    def addUsersToAlbum(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/albums/{id}/users", json=json_data)

    def getApiKeys(self) -> Dict:
        return self._request("GET", "/api-keys")

    def createApiKey(self, json_data: Dict) -> Dict:
        return self._request("POST", "/api-keys", json=json_data)

    def deleteApiKey(self, id: str) -> Dict:
        return self._request("DELETE", "/api-keys/{id}")

    def getApiKey(self, id: str) -> Dict:
        return self._request("GET", "/api-keys/{id}")

    def updateApiKey(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/api-keys/{id}", json=json_data)

    def deleteAssets(self, json_data: Dict) -> Dict:
        return self._request("DELETE", "/assets", json=json_data)

    def uploadAsset(self, key: str, x_immich_checksum: str) -> Dict:
        return self._request("POST", "/assets")

    def updateAssets(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/assets", json=json_data)

    def checkBulkUpload(self, json_data: Dict) -> Dict:
        return self._request("POST", "/assets/bulk-upload-check", json=json_data)

    def getAllUserAssetsByDeviceId(self, deviceId: str) -> Dict:
        return self._request("GET", "/assets/device/{deviceId}")

    def checkExistingAssets(self, json_data: Dict) -> Dict:
        return self._request("POST", "/assets/exist", json=json_data)

    def runAssetJobs(self, json_data: Dict) -> Dict:
        return self._request("POST", "/assets/jobs", json=json_data)

    def getMemoryLane(self, day: str, month: str) -> Dict:
        return self._request("GET", "/assets/memory-lane")

    def getRandom(self, count: str) -> Dict:
        return self._request("GET", "/assets/random")

    def getAssetStatistics(self, isArchived: str, isFavorite: str, isTrashed: str) -> Dict:
        return self._request("GET", "/assets/statistics")

    def getAssetInfo(self, id: str, key: str) -> Dict:
        return self._request("GET", "/assets/{id}")

    def updateAsset(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/assets/{id}", json=json_data)

    def downloadAsset(self, id: str, key: str) -> Dict:
        return self._request("GET", "/assets/{id}/original")

    def replaceAsset(self, id: str, key: str) -> Dict:
        return self._request("PUT", "/assets/{id}/original")

    def viewAsset(self, id: str, key: str, size: str) -> Dict:
        return self._request("GET", "/assets/{id}/thumbnail")

    def playAssetVideo(self, id: str, key: str) -> Dict:
        return self._request("GET", "/assets/{id}/video/playback")

    def getAuditDeletes(self, after: str, entityType: str, userId: str) -> Dict:
        return self._request("GET", "/audit/deletes")

    def signUpAdmin(self, json_data: Dict) -> Dict:
        return self._request("POST", "/auth/admin-sign-up", json=json_data)

    def changePassword(self, json_data: Dict) -> Dict:
        return self._request("POST", "/auth/change-password", json=json_data)

    def login(self, json_data: Dict) -> Dict:
        return self._request("POST", "/auth/login", json=json_data)

    def logout(self) -> Dict:
        return self._request("POST", "/auth/logout")

    def validateAccessToken(self) -> Dict:
        return self._request("POST", "/auth/validateToken")

    def downloadArchive(self, key: str, json_data: Dict) -> Dict:
        return self._request("POST", "/download/archive", json=json_data)

    def getDownloadInfo(self, key: str, json_data: Dict) -> Dict:
        return self._request("POST", "/download/info", json=json_data)

    def getAssetDuplicates(self) -> Dict:
        return self._request("GET", "/duplicates")

    def getFaces(self, id: str) -> Dict:
        return self._request("GET", "/faces")

    def reassignFacesById(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/faces/{id}", json=json_data)

    def getAllJobsStatus(self) -> Dict:
        return self._request("GET", "/jobs")

    def createJob(self, json_data: Dict) -> Dict:
        return self._request("POST", "/jobs", json=json_data)

    def sendJobCommand(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/jobs/{id}", json=json_data)

    def getAllLibraries(self) -> Dict:
        return self._request("GET", "/libraries")

    def createLibrary(self, json_data: Dict) -> Dict:
        return self._request("POST", "/libraries", json=json_data)

    def deleteLibrary(self, id: str) -> Dict:
        return self._request("DELETE", "/libraries/{id}")

    def getLibrary(self, id: str) -> Dict:
        return self._request("GET", "/libraries/{id}")

    def updateLibrary(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/libraries/{id}", json=json_data)

    def scanLibrary(self, id: str) -> Dict:
        return self._request("POST", "/libraries/{id}/scan")

    def getLibraryStatistics(self, id: str) -> Dict:
        return self._request("GET", "/libraries/{id}/statistics")

    def validate(self, id: str, json_data: Dict) -> Dict:
        return self._request("POST", "/libraries/{id}/validate", json=json_data)

    def getMapMarkers(self, fileCreatedAfter: str, fileCreatedBefore: str, isArchived: str, isFavorite: str, withPartners: str, withSharedAlbums: str) -> Dict:
        return self._request("GET", "/map/markers")

    def reverseGeocode(self, lat: str, lon: str) -> Dict:
        return self._request("GET", "/map/reverse-geocode")

    def searchMemories(self) -> Dict:
        return self._request("GET", "/memories")

    def createMemory(self, json_data: Dict) -> Dict:
        return self._request("POST", "/memories", json=json_data)

    def deleteMemory(self, id: str) -> Dict:
        return self._request("DELETE", "/memories/{id}")

    def getMemory(self, id: str) -> Dict:
        return self._request("GET", "/memories/{id}")

    def updateMemory(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/memories/{id}", json=json_data)

    def removeMemoryAssets(self, id: str, json_data: Dict) -> Dict:
        return self._request("DELETE", "/memories/{id}/assets", json=json_data)

    def addMemoryAssets(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/memories/{id}/assets", json=json_data)

    def getNotificationTemplate(self, name: str, json_data: Dict) -> Dict:
        return self._request("POST", "/notifications/templates/{name}", json=json_data)

    def sendTestEmail(self, json_data: Dict) -> Dict:
        return self._request("POST", "/notifications/test-email", json=json_data)

    def startOAuth(self, json_data: Dict) -> Dict:
        return self._request("POST", "/oauth/authorize", json=json_data)

    def finishOAuth(self, json_data: Dict) -> Dict:
        return self._request("POST", "/oauth/callback", json=json_data)

    def linkOAuthAccount(self, json_data: Dict) -> Dict:
        return self._request("POST", "/oauth/link", json=json_data)

    def redirectOAuthToMobile(self) -> Dict:
        return self._request("GET", "/oauth/mobile-redirect")

    def unlinkOAuthAccount(self) -> Dict:
        return self._request("POST", "/oauth/unlink")

    def getPartners(self, direction: str) -> Dict:
        return self._request("GET", "/partners")

    def removePartner(self, id: str) -> Dict:
        return self._request("DELETE", "/partners/{id}")

    def createPartner(self, id: str) -> Dict:
        return self._request("POST", "/partners/{id}")

    def updatePartner(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/partners/{id}", json=json_data)

    def getAllPeople(self, closestAssetId: str, closestPersonId: str, page: str, size: str, withHidden: str) -> Dict:
        return self._request("GET", "/people")

    def createPerson(self, json_data: Dict) -> Dict:
        return self._request("POST", "/people", json=json_data)

    def updatePeople(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/people", json=json_data)

    def getPerson(self, id: str) -> Dict:
        return self._request("GET", "/people/{id}")

    def updatePerson(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/people/{id}", json=json_data)

    def mergePerson(self, id: str, json_data: Dict) -> Dict:
        return self._request("POST", "/people/{id}/merge", json=json_data)

    def reassignFaces(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/people/{id}/reassign", json=json_data)

    def getPersonStatistics(self, id: str) -> Dict:
        return self._request("GET", "/people/{id}/statistics")

    def getPersonThumbnail(self, id: str) -> Dict:
        return self._request("GET", "/people/{id}/thumbnail")

    def getAuditFiles(self) -> Dict:
        return self._request("GET", "/reports")

    def getFileChecksums(self, json_data: Dict) -> Dict:
        return self._request("POST", "/reports/checksum", json=json_data)

    def fixAuditFiles(self, json_data: Dict) -> Dict:
        return self._request("POST", "/reports/fix", json=json_data)

    def getAssetsByCity(self) -> Dict:
        return self._request("GET", "/search/cities")

    def getExploreData(self) -> Dict:
        return self._request("GET", "/search/explore")

    def searchAssets(self, json_data: Dict) -> Dict:
        return self._request("POST", "/search/metadata", json=json_data)

    def searchPerson(self, name: str, withHidden: str) -> Dict:
        return self._request("GET", "/search/person")

    def searchPlaces(self, name: str) -> Dict:
        return self._request("GET", "/search/places")

    def searchRandom(self, json_data: Dict) -> Dict:
        return self._request("POST", "/search/random", json=json_data)

    def searchSmart(self, json_data: Dict) -> Dict:
        return self._request("POST", "/search/smart", json=json_data)

    def getSearchSuggestions(self, country: str, includeNull: str, make: str, model: str, state: str, type: str) -> Dict:
        return self._request("GET", "/search/suggestions")

    def getAboutInfo(self) -> Dict:
        return self._request("GET", "/server/about")

    def getServerConfig(self) -> Dict:
        return self._request("GET", "/server/config")

    def getServerFeatures(self) -> Dict:
        return self._request("GET", "/server/features")

    def deleteServerLicense(self) -> Dict:
        return self._request("DELETE", "/server/license")

    def getServerLicense(self) -> Dict:
        return self._request("GET", "/server/license")

    def setServerLicense(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/server/license", json=json_data)

    def getSupportedMediaTypes(self) -> Dict:
        return self._request("GET", "/server/media-types")

    def pingServer(self) -> Dict:
        return self._request("GET", "/server/ping")

    def getServerStatistics(self) -> Dict:
        return self._request("GET", "/server/statistics")

    def getStorage(self) -> Dict:
        return self._request("GET", "/server/storage")

    def getTheme(self) -> Dict:
        return self._request("GET", "/server/theme")

    def getServerVersion(self) -> Dict:
        return self._request("GET", "/server/version")

    def getVersionHistory(self) -> Dict:
        return self._request("GET", "/server/version-history")

    def deleteAllSessions(self) -> Dict:
        return self._request("DELETE", "/sessions")

    def getSessions(self) -> Dict:
        return self._request("GET", "/sessions")

    def deleteSession(self, id: str) -> Dict:
        return self._request("DELETE", "/sessions/{id}")

    def getAllSharedLinks(self) -> Dict:
        return self._request("GET", "/shared-links")

    def createSharedLink(self, json_data: Dict) -> Dict:
        return self._request("POST", "/shared-links", json=json_data)

    def getMySharedLink(self, key: str, password: str, token: str) -> Dict:
        return self._request("GET", "/shared-links/me")

    def removeSharedLink(self, id: str) -> Dict:
        return self._request("DELETE", "/shared-links/{id}")

    def getSharedLinkById(self, id: str) -> Dict:
        return self._request("GET", "/shared-links/{id}")

    def updateSharedLink(self, id: str, json_data: Dict) -> Dict:
        return self._request("PATCH", "/shared-links/{id}", json=json_data)

    def removeSharedLinkAssets(self, id: str, key: str, json_data: Dict) -> Dict:
        return self._request("DELETE", "/shared-links/{id}/assets", json=json_data)

    def addSharedLinkAssets(self, id: str, key: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/shared-links/{id}/assets", json=json_data)

    def deleteStacks(self, json_data: Dict) -> Dict:
        return self._request("DELETE", "/stacks", json=json_data)

    def searchStacks(self, primaryAssetId: str) -> Dict:
        return self._request("GET", "/stacks")

    def createStack(self, json_data: Dict) -> Dict:
        return self._request("POST", "/stacks", json=json_data)

    def deleteStack(self, id: str) -> Dict:
        return self._request("DELETE", "/stacks/{id}")

    def getStack(self, id: str) -> Dict:
        return self._request("GET", "/stacks/{id}")

    def updateStack(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/stacks/{id}", json=json_data)

    def getDeltaSync(self, json_data: Dict) -> Dict:
        return self._request("POST", "/sync/delta-sync", json=json_data)

    def getFullSyncForUser(self, json_data: Dict) -> Dict:
        return self._request("POST", "/sync/full-sync", json=json_data)

    def getConfig(self) -> Dict:
        return self._request("GET", "/system-config")

    def updateConfig(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/system-config", json=json_data)

    def getConfigDefaults(self) -> Dict:
        return self._request("GET", "/system-config/defaults")

    def getStorageTemplateOptions(self) -> Dict:
        return self._request("GET", "/system-config/storage-template-options")

    def getAdminOnboarding(self) -> Dict:
        return self._request("GET", "/system-metadata/admin-onboarding")

    def updateAdminOnboarding(self, json_data: Dict) -> Dict:
        return self._request("POST", "/system-metadata/admin-onboarding", json=json_data)

    def getReverseGeocodingState(self) -> Dict:
        return self._request("GET", "/system-metadata/reverse-geocoding-state")

    def getAllTags(self) -> Dict:
        return self._request("GET", "/tags")

    def createTag(self, json_data: Dict) -> Dict:
        return self._request("POST", "/tags", json=json_data)

    def upsertTags(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/tags", json=json_data)

    def bulkTagAssets(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/tags/assets", json=json_data)

    def deleteTag(self, id: str) -> Dict:
        return self._request("DELETE", "/tags/{id}")

    def getTagById(self, id: str) -> Dict:
        return self._request("GET", "/tags/{id}")

    def updateTag(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/tags/{id}", json=json_data)

    def untagAssets(self, id: str, json_data: Dict) -> Dict:
        return self._request("DELETE", "/tags/{id}/assets", json=json_data)

    def tagAssets(self, id: str, json_data: Dict) -> Dict:
        return self._request("PUT", "/tags/{id}/assets", json=json_data)

    def getTimeBucket(self, albumId: str, isArchived: str, isFavorite: str, isTrashed: str, key: str, order: str, personId: str, size: str, tagId: str, timeBucket: str, userId: str, withPartners: str, withStacked: str) -> Dict:
        return self._request("GET", "/timeline/bucket")

    def getTimeBuckets(self, albumId: str, isArchived: str, isFavorite: str, isTrashed: str, key: str, order: str, personId: str, size: str, tagId: str, userId: str, withPartners: str, withStacked: str) -> Dict:
        return self._request("GET", "/timeline/buckets")

    def emptyTrash(self) -> Dict:
        return self._request("POST", "/trash/empty")

    def restoreTrash(self) -> Dict:
        return self._request("POST", "/trash/restore")

    def restoreAssets(self, json_data: Dict) -> Dict:
        return self._request("POST", "/trash/restore/assets", json=json_data)

    def searchUsers(self) -> Dict:
        return self._request("GET", "/users")

    def getMyUser(self) -> Dict:
        return self._request("GET", "/users/me")

    def updateMyUser(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/users/me", json=json_data)

    def deleteUserLicense(self) -> Dict:
        return self._request("DELETE", "/users/me/license")

    def getUserLicense(self) -> Dict:
        return self._request("GET", "/users/me/license")

    def setUserLicense(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/users/me/license", json=json_data)

    def getMyPreferences(self) -> Dict:
        return self._request("GET", "/users/me/preferences")

    def updateMyPreferences(self, json_data: Dict) -> Dict:
        return self._request("PUT", "/users/me/preferences", json=json_data)

    def deleteProfileImage(self) -> Dict:
        return self._request("DELETE", "/users/profile-image")

    def createProfileImage(self) -> Dict:
        return self._request("POST", "/users/profile-image")

    def getUser(self, id: str) -> Dict:
        return self._request("GET", "/users/{id}")

    def getProfileImage(self, id: str) -> Dict:
        return self._request("GET", "/users/{id}/profile-image")

    def getAssetsByOriginalPath(self, path: str) -> Dict:
        return self._request("GET", "/view/folder")

    def getUniqueOriginalPaths(self) -> Dict:
        return self._request("GET", "/view/folder/unique-paths")
