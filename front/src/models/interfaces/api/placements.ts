export interface UpdatePlacementParams {
  session_token: string;
  activity_token: string;
  left: number;
  top: number;
}

export interface PlacementApiInterface {
  session_token: string;
  activity_token: string;
  left: number;
  top: number;
  created_at?: string | Date;
  updated_at?: string | Date;
}
