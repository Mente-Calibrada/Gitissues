# ==============================================================================
# |                                                                            |
# |  GGGGGG  IIII TTTTTT  IIII  SSSSS   SSSSS  UU   UU EEEEEE   SSSSS  |
# | GG    GG  II    TT     II  SS   SS SS   SS UU   UU EE      SS   SS |
# | GG        II    TT     II  SS      SS      UU   UU EEEE     SS      |
# | GG   GGG  II    TT     II   SSSSS   SSSSS  UU   UU EEEEE     SSSSS  |
# | GG    GG  II    TT     II       SS      SS UU   UU EE            SS |
# |  GGGGGG  IIII   TT    IIII  SSSSS   SSSSS   UUUUU  EEEEEE  SSSSS  |
# |                                                                            |
# |============================================================================|
# |                                                                            |
# |  Topological Recursive Engine - Gitissues (v1.0.0 - A P E X )              |
# |                                                                            |
# |  Sovereign Creator: Jean Laris                                             |
# |  Holding: Alantec - Architects of the Future                               |
# |  Purpose: Attraction Basin Engineering & Extreme Morphological Synthesis   |
# |  GitHub HQ: https://github.com/Calibrated-Mind/Gitissues                   |
# |                                                                            |
# |============================================================================|
# |                                                                            |
# |  [ MIT License - Open Source Sovereignty Artifact ]                        |
# |                                                                            |
# |============================================================================|

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Gitissues Topological Engine", version="1.0.0")

class BasinRequest(BaseModel):
    initial_state: int = Field(..., ge=0, description="Initial non-negative integer state.")
    steps: int = Field(10, description="Maximum execution steps.")

@app.post("/basin/compute", response_model=list[int])
def compute_sovereign_basin(payload: BasinRequest):
    """
    Computes state transition trajectories through a bounded sovereign topological basin.
    """
    n = payload.initial_state
    trajectory = [n]
    seen_states = {n}
    current = n
    max_iterations = 1000
    
    for _ in range(max_iterations):
        squared = current * current
        next_state = sum(int(digit) for digit in str(squared))
        
        if next_state in seen_states:
            trajectory.append(next_state)
            break
            
        trajectory.append(next_state)
        seen_states.add(next_state)
        current = next_state
    else:
        raise HTTPException(status_code=500, detail="Iteration limit exceeded without convergence.")
        
    return trajectory

# Alantec - Architects of the Future
