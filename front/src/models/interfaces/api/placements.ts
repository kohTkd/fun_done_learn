export interface UpdatePlacementRequest {
  session_token: string;
  activity_token: string;
  left: number;
  top: number;
}

export interface PlacementResponse {
  session_token: string;
  activity_token: string;
  left: number;
  top: number;
  created_at?: string | Date;
  updated_at?: string | Date;
}
