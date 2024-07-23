from fastapi import APIRouter, HTTPException
from basemodels import DownloadRequest, SearchRequest
import methods

router = APIRouter()

# POST THUMBNAILS FOR PLANET IMAGERY
@router.post("/search")     
async def post_querydata(request: SearchRequest):
    try:
        return await methods.query_datalist(**request.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# DOWNLOAD PLANET IMAGERY
@router.post("/download")
async def download_planet(request: DownloadRequest):
    try:
        return await methods.create_download(**request.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
