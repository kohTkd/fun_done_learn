import { PlacementResponse } from './placements';

export interface NewActivityRequest {
  session_token: string;
  content: string;
}

export interface UpdateActivityRequest extends NewActivityRequest {
  token: string;
}

export interface ActivityResponse {
  session_token: string;
  token: string;
  content: string;
  created_at?: Date | string;
  updated_at?: Date | string;
  placement?: PlacementResponse;
}
