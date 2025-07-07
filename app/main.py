from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse # Add to Top
import pandas as pd
from io import BytesIO # Add to Top of File

from typing import List, Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from app.schemas.target import TargetSearchResults, Target, TargetCreate
from app.schemas.taxonomy import TaxonomySearchResults, Taxonomy, TaxonomyCreate
from app.schemas.collection_target import CollectionTargetSearchResults, CollectionTarget, CollectionTargetCreate

from app import deps
from app import crud

# Converts ?state=COMPLETED,ENQUEUED -> ?state=COMPLETED&state=ENQUEUED
# Converts ?collections=3434,4545 -> ?collections=3434&collections=4545
from app.middlewarehelper.starlettehelper import QueryStringFlatteningMiddleware

# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


app = FastAPI(title="W3ACT DB API", openapi_url="/openapi.json")
# add parameter flattener
app.add_middleware(QueryStringFlatteningMiddleware)


api_router = APIRouter()

# You now have everything you need to offer JSON, CSV and XLSX

@api_router.get("/json")
def get_json_data():
    df = pd.DataFrame(
        [["Canada", 10], ["USA", 20]], 
        columns=["team", "points"]
    )
    return df.to_dict(orient="records")

# 'http://localhost:5000/xlsx' \
#  -H 'accept: application/json' \
#  --output asd.xlsx

@api_router.get("/xlsx")
def get_excel_data():
    df = pd.DataFrame(
        [["Canada", 10], ["USA", 20]], 
        columns=["team", "points"]
    )
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        df.to_excel(writer, index=False)
    return StreamingResponse(
        BytesIO(buffer.getvalue()),
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={"Content-Disposition": "attachment; filename=data.xlsx"}
)

@api_router.get("/csv")
def get_csv_data():
    df = pd.DataFrame(
        [["Canada", 10], ["USA", 20]], 
        columns=["team", "points"]
    )
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=data.csv"}
)

# Is it possible to do:
# http://localhost/item?num=1,2,3,4,5,6
# instead of:
# http://localhost/item?num=1&num=2&num=3&num=4&num=5&num=6?
#
# starlette gives query parameter num="1,2,3,4,5,6", and pydantic doesn't know how to parse "1,2,3,4,5,6"

@api_router.get("/tocsv", status_code=200, response_model=Taxonomy)
def fetch_sql_query(
    *,
    x_id: int,
    q: List[int] = Query(None),
    dbSession: Session = Depends(deps.get_db),
) -> None :
    """
    Fetch a single SQL 
    COPY commands are only supported using the CopyManager API.
    """
    #cur = db.cursor()
    #cursor = session.execute(sql).cursor
    # cursor = dbSession.execute(sql).cursor
    cur = dbSession.connection().connection.cursor()

    with open('out.csv', 'w') as f:
        cur.copy_expert('COPY taxonomy TO STDOUT WITH CSV HEADER', f)
    print("Table exported to CSV!")

    #headers = {'Content-Disposition': 'inline; filename="out.csv"'}
    #return Response(bytes(out), headers=headers, media_type='application/csv')



    # ------------
    # result = crud.recipe.get(db=db, id=recipe_id)
    # if not result:
    #     # the exception is raised, not returned - you will get a validation
    #     # error otherwise.
    #     raise HTTPException(
    #         status_code=404, detail=f"Recipe with ID {recipe_id} not found"
    #     )

    # return result
    return None

def sql_to_dataframe(conn, query, column_names):
   """ 
   Import data from a PostgreSQL database using a SELECT query 
   """
   cursor = conn.cursor()
   try:
      cursor.execute(query)
   except (Exception, deps.get_db.DatabaseError) as error:
      print("Error: %s" % error)
   cursor.close()
   return 1
   # The execute returns a list of tuples:
   tuples_list = cursor.fetchall()
   cursor.close()
   # Now we need to transform the list into a pandas DataFrame:
   df = pd.DataFrame(tuples_list, columns=column_names)
   return df

@api_router.get("/collectiontarget/{collection_id}", response_model=CollectionTarget)
def get_collection(
        collection_id: int,
        # db: Session = Depends(get_db),
        db: Session = Depends(deps.get_db)

):
    """API endpoint to get a specific blog by blog_id"""
    collectionList = db.query(CollectionTarget).first()
    # targetList = db.query(CollectionTarget).filter(CollectionTarget.target_id == collection_id).first()
    if not collectionList:
        raise HTTPException(status_code=404, detail="Collections or Targets not found")
    return collectionList


@api_router.get("/collectiontarget2/{collection_id}", response_model=Taxonomy)
def get_collection_fromTaxonomyPerspective(
        collection_id: int,
        # db: Session = Depends(get_db),
        db: Session = Depends(deps.get_db)
):
    """API endpoint to get a specific blog by blog_id"""
    collectionList = db.query(Taxonomy).first()
    # targetList = db.query(CollectionTarget).filter(CollectionTarget.target_id == collection_id).first()
    if not collectionList:
        raise HTTPException(status_code=404, detail="Collections or Targets not found")
    return collectionList




@api_router.get("/csvdataset")
def get_csv_dataset():


    #creating a query variable to store our query to pass into the function
    query = """ SELECT id, 
                    title, 
                    url 
                FROM target
            """
    #creating a list with columns names to pass into the function
    column_names = ['id','title', 'url']
    #opening the connection
    conn = deps.get_db
    #loading our dataframe
    df = sql_to_dataframe(conn, query, column_names)
    #closing the connection
    #conn.close()
    # Let’s see if we loaded the df successfully
    df.head()



    # df = pd.DataFrame(
    #     [["Canada", 10], ["USA", 20]], 
    #     columns=["team", "points"]
    # )
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=data.csv"}
)



@api_router.get("/targets", status_code=200)
def actdb_targets(
    request: Request,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Root GET
    """


    # TOP level - parent_id isnull
    # select * from taxonomy where parent_id isnull and ttype = 'collections'
    # Sub collections - parent_id NOT null
    # select * from taxonomy where ttype = 'collections' and id = 4278


    collections = crud.taxonomy.get_multi(db=db, limit=20) 
    # db_item = db.query(Item).filter(Item.id == item_id).first()

    
    # select * from taxonomy where parent_id isnull and ttype = 'subject'
    subjects = crud.target.get_multi(db=db, limit=2)

    targets = crud.target.get_multi(db=db, limit=10)
    print("hi")
    return TEMPLATES.TemplateResponse(
        "targets.html",
        {"request": request, "targets": targets, "collections": collections }
    )


@api_router.get("/taxonomy/{taxonomy_id}", status_code=200, response_model=Taxonomy)
def fetch_taxonomy(
    *,
    taxonomy_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = crud.taxonomy.get(db=db, id=taxonomy_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Taxonomy with ID {taxonomy_id} not found"
        )

    return result



app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
