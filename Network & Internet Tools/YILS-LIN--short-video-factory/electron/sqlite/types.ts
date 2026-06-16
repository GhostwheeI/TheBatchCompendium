export interface QueryParams {
  sql: string
  params?: any[]
}

export interface InsertParams {
  table: string
  data: { [key: string]: any }
}

export interface UpdateParams {
  table: string
  data: { [key: string]: any }
  condition: string
}

export interface DeleteParams {
  table: string
  condition: string
}

export interface BulkInsertOrUpdateParams {
  table: string
  data: any[]
}
